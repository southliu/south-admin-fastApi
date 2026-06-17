from typing import Optional, List

from schemas.base import CamelModel


class CreateMenuRequest(CamelModel):
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


class UpdateMenuRequest(CamelModel):
    label: str
    label_en: str
    type: Optional[int] = None
    icon: Optional[str] = None
    router: Optional[str] = None
    rule: Optional[str] = None
    order: Optional[int] = None
    state: Optional[int] = None
    parent_id: Optional[int] = None


class ChangeMenuStateRequest(CamelModel):
    id: int
    state: int


class BatchDeleteRequest(CamelModel):
    ids: List[int]
