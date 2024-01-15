from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr
class Ad_create(Document):
    type : Optional[str] = None
    brand : Optional[str] = None
    contents : Optional[str] = None
    thumnail : Optional[str] = None
    thumnail_url : Optional[str] = None
    detail_contents : Optional[str] = None
    point : Optional[int] = None

    class Settings:
        name = "ad_create"
