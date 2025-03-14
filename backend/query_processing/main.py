from fastapi import FastAPI, HTTPException, Depends, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
import jwt
from llama3_integration import process_query_with_llama

app = FastAPI(title="Query Processing Service")
app.add_middleware(
CORSMiddleware,
allow_origins=["http://localhost:3000"], # adjust as needed
allow_credentials=True,
allow_methods=[""],
allow_headers=[""],
)


@app.middleware("http")
async def options_interceptor(request: Request, call_next):
    if request.method.upper() == "OPTIONS":
        return Response(
            status_code=200,
            headers={
                "Access-Control-Allow-Origin": "http://localhost:3000",
                "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
                "Access-Control-Allow-Headers": "*",
                },
            )
    return await call_next(request)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/token")
SECRET_KEY = "d51d585e568c4134b0d122d264956c37358c8ba49bd6c5da72f0328e88e43ffc"

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/query/process_query")
def process_query(query: dict, token_data: dict = Depends(verify_token)):
    user = token_data.get("sub")
    if not user:
        raise HTTPException(status_code=401, detail="User not authenticated")
    try:
        received_query = query.get("query", "")
        print("Received query:", received_query)


    # Call your Llama integration function:
        answer = process_query_with_llama(received_query)
        print("Generated answer:", answer)
    
        return {"answer": answer}
    except Exception as e:
        print("Error in process_query:", e)
        raise HTTPException(status_code=500, detail=f"Error processing query: {e}")