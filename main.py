from contextlib import asynccontextmanager
from fastapi import FastAPI

from core.router import api_router
from core.database import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时创建数据库表
    await create_tables()
    yield


app = FastAPI(title="South Admin API", version="0.1.0", lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(api_router)
