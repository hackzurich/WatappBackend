from fastapi import FastAPI
from datetime import datetime

# Create API objects
app = FastAPI()

@app.get("/healthz")
async def health():
    """Health probe that responds with a simple message."""
    return {
        "message": "healthy",
        "timestamp": datetime.now()
    }