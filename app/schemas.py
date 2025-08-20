from pydantic import BaseModel, Field


class AddRequest(BaseModel):
    x: float = Field(..., description="first operand")
    y: float = Field(..., description="second operand")


class AddResult(BaseModel):
    result: float
