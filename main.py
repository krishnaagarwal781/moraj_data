from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
from pathlib import Path

app = FastAPI()

# Path to the JSON file
json_file_path = Path("data.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get-data")
async def get_data():
    if not json_file_path.exists():
        raise HTTPException(status_code=404, detail="JSON file not found")
    
    with open(json_file_path, "r") as file:
        data = json.load(file)
    
    return data


