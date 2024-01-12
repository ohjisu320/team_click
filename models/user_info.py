from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr
class User_info(Document):
    user_name : Optional[str] = None
    user_id : Optional[str] = None
    user_pswd: Optional[str] = None
    user_phone_num1: Optional[int] = None
    user_email: Optional[str] = None
    user_auth1 : Optional[str] = None
    user_auth2 : Optional[str] = None
    user_auth3 : Optional[str] = None
    user_auth4 : Optional[str] = None
    user_point : Optional[int] = None
    

    class Settings:
        name = "user_info"
