from typing import Any, List, Optional

from schemas.base import CamelModel


class ResponseModel(CamelModel):
    code: int = 200
    message: str = "success"
    data: Any = None


class PageData(CamelModel):
    items: List[Any] = []
    page: int = 1
    page_size: int = 10
    total: int = 0
    total_pages: int = 0
