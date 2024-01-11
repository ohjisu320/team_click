from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request


router = APIRouter()

templates = Jinja2Templates(directory="templates/")

# 로고 클릭했을 때 : 주소 /clicktech/
@router.get("/") # 펑션 호출 방식
async def usermain(request:Request):
    return templates.TemplateResponse(name="usermain.html", context={'request':request})

# Log-in 클릭했을 때 : 주소 /clicktech/login # !!html 수정 전!! #
@router.get("/login") # 펑션 호출 방식
async def login(request:Request):
    return templates.TemplateResponse(name="usermain.html", context={'request':request}) 

# Sign-in 클릭했을 때 : 주소 /clicktech/signin
@router.get("/signin") # 펑션 호출 방식
async def signin(request:Request):
    return templates.TemplateResponse(name="join/step1.html", context={'request':request})

# 전체리스트 클릭했을 때 : 주소 /clicktech/alllist
@router.get("/alllist") # 펑션 호출 방식
async def allad(request:Request):
    return templates.TemplateResponse(name="offerwall/allad.html", context={'request':request})


# 쿠폰교환 클릭했을 때 : 주소 /clicktech/exchange
@router.get("/exchange") # 펑션 호출 방식
async def exchange(request:Request):
    return templates.TemplateResponse(name="exchange/gifticon_main.html", context={'request':request})

# 쿠폰교환페이지에서 쿠폰 하나를 클릭했을 때 : 주소 /clicktech/exchange/detail
@router.get("/exchange/detail") # 펑션 호출 방식
async def exchange(request:Request):
    return templates.TemplateResponse(name="exchange/gifticon_detail.html", context={'request':request})

# 공지사항 클릭했을 때 : 주소 /clicktech/notice
@router.get("/notice") # 펑션 호출 방식
async def notice(request:Request):
    return templates.TemplateResponse(name="notice/notice_main.html", context={'request':request})

# 공지사항의 글 하나를 클릭했을 때 : 주소 /clicktech/notice/detail
@router.get("/notice/detail") # 펑션 호출 방식
async def notice(request:Request):
    return templates.TemplateResponse(name="notice/notice_main.html", context={'request':request})

# FAQ 클릭했을 때 : 주소 /clicktech/faq
@router.get("/faq") # 펑션 호출 방식
async def faq(request:Request):
    return templates.TemplateResponse(name="faq/faq_main.html", context={'request':request})

# FAQ의 글 하나를 클릭했을 때 : 주소 /clicktech/faq
@router.get("/faq/detail") # 펑션 호출 방식
async def faq(request:Request):
    return templates.TemplateResponse(name="faq/faq_detail.html", context={'request':request})
