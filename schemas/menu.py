from typing import Optional, List

from pydantic import BaseModel


class CreateMenuRequest(BaseModel):
    label: str
    label_en: str
    type: int
    icon: Optional[str] = None
    router: Optional[str] = None
    rule: Optional[str] = None
    order: int = 0
    state: int = 1
    parent_id: Optional[int] = None
    actions: Optional[List[str]] = None


class UpdateMenuRequest(BaseModel):
    label: str
    label_en: str
    type: Optional[int] = None
    icon: Optional[str] = None
    router: Optional[str] = None
    rule: Optional[str] = None
    order: Optional[int] = None
    state: Optional[int] = None
    parent_id: Optional[int] = None


class ChangeMenuStateRequest(BaseModel):
    id: int
    state: int


class BatchDeleteRequest(BaseModel):
    ids: List[int]
