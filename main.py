from contextlib import asynccontextmanager
from fastapi import FastAPI

from core.router import api_router
from core.database import create_tables
from middleware.log import LogMiddleware
from middleware.auth import AuthError, auth_error_handler


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时创建数据库表
    await create_tables()
    yield


app = FastAPI(title="South Admin API", version="0.1.0", lifespan=lifespan)

# 注册认证异常处理器
app.add_exception_handler(AuthError, auth_error_handler)

# 注册日志中间件
app.add_middleware(LogMiddleware)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(api_router)
