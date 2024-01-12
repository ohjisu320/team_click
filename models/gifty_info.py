from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr
class Gifty_info(Document):
    brand_name : Optional[str] = None
    gifty_name : Optional[str] = None
    origin_price : Optional[str] = None
    discount_price: Optional[str] = None
    discount_rate: Optional[int] = None
    gifty_detail : Optional[str] = None
    gifty_caution : Optional[str] = None
    image_path: Optional[str] = None
    # 뤼튼의 설명으로는 이미지를 직접 같이 저장하는 것은 비효율적이라
    # 서버의 디렉토리에 저장하고, 끌고 갈 경로를 지정하는 것이 낫다고 함
    # 그러나, Selenium으로 긁어올 때 이미지도 같이 mongo에 저장되는 여부를 모르므로 변경 가능성 있음

    class Settings:
        name = "gifty_info"
