from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import status
app = FastAPI()

class Name(BaseModel):
    name: str
    times: int = 1

@app.post("/name", status_code=status.HTTP_201_CREATED)
def name(payload: Name):
    return [payload.name] * payload.times
