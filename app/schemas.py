from pydantic import BaseModel, Field

class PredictRequest(BaseModel):
    area: float = Field(..., gt=0)
    rooms: int = Field(..., ge=0)

class PredictResponse(BaseModel):
    predicted_price: int
    currency: str = "EUR"
    model_type: str = "mock_constant"

