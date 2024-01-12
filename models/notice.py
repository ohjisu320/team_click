from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr
class Notice(Document):
    notice_title : Optional[str] = None
    main_text : Optional[str] = None
    date : Optional[str] = None

    class Settings:
        name = "notice"
