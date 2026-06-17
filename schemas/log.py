from typing import Optional

from schemas.base import CamelModel


class CreateLogRequest(CamelModel):
    username: Optional[str] = None
    ip: Optional[str] = None
    method: Optional[str] = None
    url: Optional[str] = None
    params: Optional[str] = None
    user_agent: Optional[str] = None
    status: Optional[str] = None
    error: Optional[str] = None
    latency: int = 0
    type: int = 0
