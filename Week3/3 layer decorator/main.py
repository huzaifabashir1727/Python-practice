from fastapi import FastAPI
from decorators import retry
import requests

app = FastAPI()

@retry(max_attempts=3)
def fetch_external_data():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    return response.json()

@app.get("/data")
def get_data():
    return fetch_external_data()