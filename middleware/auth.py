from fastapi import Depends, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from config.database import get_db
from utils.security import decode_access_token
from crud.user import get_user_by_id

security = HTTPBearer(auto_error=False)


async def get_current_user(
    request: Request,
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
):
    """获取当前用户"""
    if not credentials:
        return JSONResponse(
            status_code=200,
            content={"code": 401, "data": "", "message": "无效权限访问"},
        )

    token = credentials.credentials
    payload = decode_access_token(token)

    if payload is None:
        return JSONResponse(
            status_code=200,
            content={"code": 401, "data": "", "message": "无效权限访问"},
        )

    user_id = payload.get("sub")
    if user_id is None:
        return JSONResponse(
            status_code=200,
            content={"code": 401, "data": "", "message": "无效权限访问"},
        )

    user = await get_user_by_id(db, int(user_id))
    if user is None:
        return JSONResponse(
            status_code=200,
            content={"code": 401, "data": "", "message": "无效权限访问"},
        )

    return user


def get_user_permissions(user) -> list:
    """获取用户权限列表"""
    permission_set = set()
    for role in user.roles:
        for menu in role.menus:
            if menu.permission:
                permission_set.add(menu.permission.name)
    return list(permission_set)


def get_user_role_ids(user) -> list:
    """获取用户角色ID列表"""
    return [role.id for role in user.roles]
