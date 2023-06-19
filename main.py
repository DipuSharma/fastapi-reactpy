from fastapi import FastAPI
from reactpy.backend.fastapi import configure

from src.main_component import MainComponent

app = FastAPI()
configure(app, MainComponent)