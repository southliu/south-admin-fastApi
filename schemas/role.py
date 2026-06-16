from typing import Optional, List

from pydantic import BaseModel


class CreateRoleRequest(BaseModel):
    name: str
    description: Optional[str] = None
    authorize: Optional[List[int]] = None


class UpdateRoleRequest(BaseModel):
    name: str
    description: Optional[str] = None
    authorize: Optional[List[int]] = None


class AuthorizeRoleRequest(BaseModel):
    role_id: int
    menu_ids: List[int]
