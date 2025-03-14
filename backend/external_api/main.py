from fastapi import FastAPI

app = FastAPI(title="External API Integration Service")

@app.post("/simulate_payment")
def simulate_payment(payment_info: dict):
# Simulate processing a payment.
    return {"status": "success", "transaction_id": "TX123456789"}

@app.get("/market_data")
def get_market_data():
# Simulate retrieving market data.
    return {"market": "Simulated Market Data", "trend": "upward"}