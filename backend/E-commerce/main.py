from fastapi import FastAPI
from . import database, models

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.get('/')
def default():
    return "welcome"