from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.dependencies.database import init_db
from app.routers import prompt

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize storage on startup
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Add your React app's URL here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(prompt.router, prefix="/api/v1") 