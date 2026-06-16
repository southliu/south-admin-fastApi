from typing import Any, List, Optional

from pydantic import BaseModel


class ResponseModel(BaseModel):
    code: int = 200
    message: str = "success"
    data: Any = None


class PageData(BaseModel):
    items: List[Any] = []
    page: int = 1
    page_size: int = 10
    total: int = 0
    total_pages: int = 0
