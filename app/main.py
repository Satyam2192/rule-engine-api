from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routers import rule_router
from .database import init_db, close_db
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]  # Adjust as needed for your use case

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await close_db()

# Attach the lifespan context manager to the app
app = FastAPI(lifespan=lifespan)

app.include_router(rule_router.router)
