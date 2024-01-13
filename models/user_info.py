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
    user_terms1: Optional[str] = None
    user_terms2: Optional[str] = None
    user_terms3: Optional[str] = None
    user_terms4: Optional[str] = None

    class Settings:
        name = "user_info"
