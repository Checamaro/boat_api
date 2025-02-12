from fastapi import FastAPI
from src.models.rowboat import Rowboat
from src.utils.logger import logger
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
boat = Rowboat(name="Titanic", capacity=4, oars=2)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Можно указать ["http://127.0.0.1:8001"] для безопасности
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/move/{direction}")
def move(direction: str):
    if direction in ["forward", "backward", "left", "right"]:
        boat.move(direction)
        logger.info(f"Boat moved {direction}")
        return {"message": f"Boat moved {direction}"}
    return {"error": "Invalid direction"}

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
    uvicorn.run(app, host="127.0.0.1", port=5000, reload=True)
