from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.services.scraper import Scraper


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifecycle manager"""
    print("Starting up the application...")

    listed_urls = Scraper().get_listed_companies_url()

    try:
        yield
    finally:
        print("Shutting down the application...")


app = FastAPI(
    title="Jamaica Stock Portfolio Manager",
    description="Local application to manage and track Jamaica stock portfolio",
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health check endpoint
@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "version": app.version
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        workers=1
    )
