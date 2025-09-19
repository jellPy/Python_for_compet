from pydantic import BaseModel
from fastapi import Body
from fastapi import FastAPI, status   # импортируем фреймворк и константы

app = FastAPI()                       # создаём приложение

# Декоратор app.<METHOD>() регистрирует обработчик HTTP-метода
@app.get("/ping", status_code=status.HTTP_200_OK)
def ping() -> dict[str, bool]:
    """
    Простейший эндпоинт:
    GET /ping  →  {"pong": true}
    """
    return {"pong": True}

class Echo(BaseModel):
    message: str
    times: int = 1

@app.post("/echo", status_code=status.HTTP_201_CREATED)
def echo(payload: Echo = Body(...)):
    """
    Возвращает сообщение `times` раз.
    POST /echo
    {
      "message": "hi",
      "times": 3
    }
    → ["hi", "hi", "hi"]
    """
    return [payload.message] * payload.times