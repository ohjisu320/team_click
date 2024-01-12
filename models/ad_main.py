from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr
class Ad_main(Document):
    type : Optional[str] = None
    brand : Optional[str] = None
    contents : Optional[str] = None
    thumnail : Optional[str] = None

    class Settings:
        name = "ad_main"
