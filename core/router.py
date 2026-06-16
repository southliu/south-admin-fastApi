from fastapi import APIRouter
from api.routes.system import user, role, menu, permission, log

api_router = APIRouter(prefix="/system")

api_router.include_router(user.router)
api_router.include_router(role.router)
api_router.include_router(menu.router)
api_router.include_router(permission.router)
api_router.include_router(log.router)
