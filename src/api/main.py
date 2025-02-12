from fastapi import FastAPI, HTTPException
from src.models.rowboat import Rowboat

app = FastAPI()

boat = Rowboat(capacity=2)

@app.get("/")
def read_root():
    return {"message": "Boat API is running!"}

@app.get("/boat")
def get_boat_status():
    return {
        "capacity": boat.capacity,
        "passengers": boat.passengers,
        "position": boat.position,
        "direction": boat.direction
    }

@app.post("/boat/passenger")
def add_passenger():
    try:
        boat.add_passenger()
        return {"message": "Passenger added", "passengers": boat.passengers}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/boat/passenger")
def remove_passenger():
    try:
        boat.remove_passenger()
        return {"message": "Passenger removed", "passengers": boat.passengers}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/boat/direction/{new_direction}")
def change_direction(new_direction: str):
    try:
        boat.change_direction(new_direction)
        return {"message": f"Direction changed to {new_direction}"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/boat/move")
def move_boat():
    boat.move()
    return {"message": "Boat moved", "position": boat.position}

@app.put("/boat/stop")
def stop_boat():
    boat.stop()
    return {"message": "Boat stopped"}
