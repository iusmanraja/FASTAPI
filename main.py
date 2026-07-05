from fastapi import FastAPI
from dummy_data.app.tasks.routes import router

app = FastAPI()

app.include_router(router)