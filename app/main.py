from fastapi import FastAPI
from app.schemas import PredictRequest, PredictResponse
from app.model import predict_price

app = FastAPI(title="Apartment Price API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    price = predict_price(req.area, req.rooms)
    return PredictResponse(predicted_price=price)

