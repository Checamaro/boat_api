import os
import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.models.rowboat import Rowboat
from src.utils.logger import logger

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = FastAPI()

origins = [
    "http://localhost:8001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

boat = Rowboat(name="Titanic", capacity=4, oars=2)

@app.post("/move/forward")
def move_forward():
    boat.move("forward")
    return {"message": "Boat moved forward"}

@app.post("/move/backward")
def move_backward():
    boat.move("backward")
    return {"message": "Boat moved backward"}

@app.post("/move/left")
def move_left():
    boat.move("left")
    return {"message": "Boat moved left"}

@app.post("/move/right")
def move_right():
    boat.move("right")
    return {"message": "Boat moved right"}

@app.post("/stop")
def stop_boat():
    boat.stop()
    logger.info("Boat stopped")
    return {"message": "Boat stopped"}

@app.post("/passenger/add")
def add_passenger():
    try:
        boat.add_passenger()
        logger.info("Passenger added")
        return {"message": "Passenger added"}
    except ValueError as e:
        return {"error": str(e)}

@app.post("/passenger/remove")
def remove_passenger():
    try:
        boat.remove_passenger()
        logger.info("Passenger removed")
        return {"message": "Passenger removed"}
    except ValueError as e:
        return {"error": str(e)}

@app.get("/status")
def get_status():
    return {
        "name": boat.name,
        "capacity": boat.capacity,
        "passengers": boat.passengers,
        "direction": boat.direction,
        "oars": boat.oars
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.api.endpoints:app", host="127.0.0.1", port=5000, reload=True)