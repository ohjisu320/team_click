from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr
class User_info(Document, BaseModel):
    user_name : Optional[str] = None
    user_id : Optional[str] = None
    user_pswd: Optional[str] = None
    user_phone_num1: Optional[str] = None
    user_phone_num2: Optional[str] = None
    user_phone_num3: Optional[str] = None
    user_email: Optional[str] = None
    user_auth1: str = ""
    user_auth2: str = ""
    user_auth3: str = ""
    user_auth4: str = ""
    user_point: int = 0

    class Settings:
        name = "user_info"
