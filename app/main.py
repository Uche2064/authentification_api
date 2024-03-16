from fastapi import FastAPI
from .routers import user, auth
from .db import moteur
from . import models

app = FastAPI()

try:
    models.Base.metadata.create_all(bind=moteur)
except Exception as e:
    print(e)


app.include_router(user.router)
app.include_router(auth.router)