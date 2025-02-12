import requests

BASE_URL = "http://127.0.0.1:5000"

def move(direction):
    response = requests.post(f"{BASE_URL}/move/{direction}")
    print(response.json())

def stop():
    response = requests.post(f"{BASE_URL}/stop")
    print(response.json())

def add_passenger():
    response = requests.post(f"{BASE_URL}/passenger/add")
    print(response.json())

def remove_passenger():
    response = requests.post(f"{BASE_URL}/passenger/remove")
    print(response.json())

def get_status():
    response = requests.get(f"{BASE_URL}/status")
    print(response.json())

if __name__ == "__main__":
    get_status()
