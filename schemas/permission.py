from typing import Optional

from pydantic import BaseModel


class CreatePermissionRequest(BaseModel):
    name: str
    description: Optional[str] = None


class UpdatePermissionRequest(BaseModel):
    name: str
    description: Optional[str] = None
