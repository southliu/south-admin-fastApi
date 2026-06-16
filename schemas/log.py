from typing import Optional

from pydantic import BaseModel


class CreateLogRequest(BaseModel):
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
