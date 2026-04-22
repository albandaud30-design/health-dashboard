from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TempData(BaseModel):
    temperature: float

latest_temp = {"temperature": None}

@app.post("/api/temp")
def receive_temp(data: TempData):
    latest_temp["temperature"] = data.temperature
    return {"status": "ok"}

@app.get("/api/temp")
def get_temp():
    return latest_temp