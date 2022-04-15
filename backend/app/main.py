import os
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi_sqlalchemy import DBSessionMiddleware
from .routers.users import user
from .routers.foods import food
from .routers.foods_eaten import food_eaten
from starlette.middleware.cors import CORSMiddleware

from dotenv import load_dotenv

load_dotenv(".env")

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])
app.include_router(user.router)
app.include_router(food.router)
app.include_router(food_eaten.router)
origins = [
    "http://localhost:3000",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5050",
    "http://localhost:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["ROOT"], summary="Root redirect")
async def docs_redirect():
    return RedirectResponse(url='/docs')
