from fastapi import FastAPI
from .schemas import AddRequest, AddResult
from .service import add_numbers

app = FastAPI(title="MyApp API", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/add", response_model=AddResult)
def add(req: AddRequest):
    return add_numbers(req)
