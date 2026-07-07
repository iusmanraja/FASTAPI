from fastapi import FastAPI

from dummy_data.app.database import engine
from dummy_data.app import models
from dummy_data.app.tasks.routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)