import json as js
from pathlib import Path

HERE = Path(__file__)
DATA_PATH = HERE.parent / "data.json"
sculpture_data = js.loads(DATA_PATH.read_text())

from fastapi import FastAPI


#  Configure backend (app) and frontend (MainComponent)
from reactpy.backend.fastapi import configure

# Frontend using reactpy library
from src.main_component import MainComponent

# Backend using Fastapi 
app = FastAPI()

# Pass arguments under configure (backend, frontend)
configure(app, MainComponent)