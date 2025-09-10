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
