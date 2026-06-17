from typing import Optional

from schemas.base import CamelModel


class CreatePermissionRequest(CamelModel):
    name: str
    description: Optional[str] = None


class UpdatePermissionRequest(CamelModel):
    name: str
    description: Optional[str] = None
