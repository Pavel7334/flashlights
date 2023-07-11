from fastapi import FastAPI

from .api import router

app = FastAPI(
    title="Фонарик"
)
app.include_router(router)


