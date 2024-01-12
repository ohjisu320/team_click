from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr
class Faq(Document):
    categories : Optional[str] = None
    question_title : Optional[str] = None
    answer_main_text : Optional[str] = None

    class Settings:
        name = "faq"
