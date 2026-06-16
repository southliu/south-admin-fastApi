from typing import Optional, List

from pydantic import BaseModel


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    token: str
    user: "UserInfo"
    roles: List[int]
    permissions: List[str]


class UserInfo(BaseModel):
    id: int
    username: str
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    status: int
    roles: List[int] = []


class CreateUserRequest(BaseModel):
    username: str
    password: str
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    status: int = 1
    role_ids: List[int] = []


class UpdateUserRequest(BaseModel):
    username: str
    password: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    status: Optional[int] = None
    role_ids: Optional[List[int]] = None


class UpdatePasswordRequest(BaseModel):
    old_password: str
    new_password: str
    confirm_password: str


class RefreshPermissionsResponse(BaseModel):
    user: UserInfo
    permissions: List[str]
    roles: List[int]
