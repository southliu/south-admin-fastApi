from typing import Optional, List

from schemas.base import CamelModel


class LoginRequest(CamelModel):
    username: str
    password: str


class LoginResponse(CamelModel):
    token: str
    user: "UserInfo"
    roles: List[int]
    permissions: List[str]


class UserInfo(CamelModel):
    id: int
    username: str
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    status: int
    roles: List[int] = []


class CreateUserRequest(CamelModel):
    username: str
    password: str
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    status: int = 1
    role_ids: List[int] = []


class UpdateUserRequest(CamelModel):
    username: str
    password: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    status: Optional[int] = None
    role_ids: Optional[List[int]] = None


class UpdatePasswordRequest(CamelModel):
    old_password: str
    new_password: str
    confirm_password: str


class RefreshPermissionsResponse(CamelModel):
    user: UserInfo
    permissions: List[str]
    roles: List[int]
