from fastapi import FastAPI

from core.router import api_router

app = FastAPI(title="South Admin API", version="0.1.0")


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(api_router)
