from typing import Union, Optional
from pydantic import BaseModel


class Config(BaseModel):
    osu_client: Optional[int] = None
    osu_key: Optional[str] = None
    osu_cookie: Optional[str] = None
