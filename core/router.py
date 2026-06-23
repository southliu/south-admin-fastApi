from fastapi import APIRouter
from api.routes.system import user, role, menu, permission, log

api_router = APIRouter()

system_router = APIRouter(prefix="/system")
system_router.include_router(user.router)
system_router.include_router(role.router)
system_router.include_router(menu.router)
system_router.include_router(permission.router)
system_router.include_router(log.router)

api_router.include_router(system_router)
