from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
import jwt

app = FastAPI(title="User Management Service")

app.add_middleware(
CORSMiddleware,
allow_origins=["http://localhost:3000"],
allow_credentials=True,
allow_methods=[""],
allow_headers=[""],
)

@app.options("/user/token", include_in_schema=False)
async def options_user_token():
    # Return an empty 200 response
    return Response(status_code=200)

SECRET_KEY = "d51d585e568c4134b0d122d264956c37358c8ba49bd6c5da72f0328e88e43ffc"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/token")

users_db = {
"test@example.com": {"password": "test123", "username": "test"}
}

def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")

@app.post("/user/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)
    if not user or user["password"] != form_data.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/user/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        username = payload.get("sub")
        return {"username": username}
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")