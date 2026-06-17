from typing import Optional, List

from schemas.base import CamelModel


class CreateRoleRequest(CamelModel):
    name: str
    description: Optional[str] = None
    authorize: Optional[List[int]] = None


class UpdateRoleRequest(CamelModel):
    name: str
    description: Optional[str] = None
    authorize: Optional[List[int]] = None


class AuthorizeRoleRequest(CamelModel):
    role_id: int
    menu_ids: List[int]
