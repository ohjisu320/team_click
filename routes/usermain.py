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
    return templates.TemplateResponse(name="login/login.html", context={'request':request}) 

# Sign-in 클릭했을 때 : 주소 /clicktech/join
@router.get("/join") # 펑션 호출 방식
async def join(request:Request):
    return templates.TemplateResponse(name="join/step1.html", context={'request':request})

# Sign-in 클릭했을 때 : 주소 /clicktech/join/step2
@router.get("/join/step2") # 펑션 호출 방식
async def join(request:Request):
    return templates.TemplateResponse(name="join/step2.html", context={'request':request})

# Sign-in 클릭했을 때 : 주소 /clicktech/join
@router.get("/join/step3") # 펑션 호출 방식
async def join(request:Request):
    return templates.TemplateResponse(name="join/step3.html", context={'request':request})


# database 의 connections에 정의된 Database 클래스와 user_info collection을 정의한 User_info 클래스를 import
from databases.connections import Database
from models.user_info import User_info
collection_user = Database(User_info)
@router.post("/join/step4") # 펑션 호출 방식
async def user_input_post(request:Request):
    user_dict = dict(await request.form())
    try:
        user = User_info(**user_dict)
        await collection_user.save(user)
    except Exception as e:
        print(f"Error occurred: {e}")
        user = User_info(user_auth1="", user_auth2="", user_auth3="", user_auth4="",user_point="")
        await collection_user.save(user)
    # 리스트 정보
    user_list = await collection_user.get_all()
    return templates.TemplateResponse(name="join/step4.html"
                                      , context={'request':request, "user_info" : user_list})

# # Sign-in 클릭했을 때 : 주소 /clicktech/join
# @router.get("/join/step4") # 펑션 호출 방식
# async def join(request:Request):
#     return templates.TemplateResponse(name="join/step4.html", context={'request':request})

# 전체리스트 클릭했을 때 : 주소 /clicktech/alllist
@router.get("/alllist") # 펑션 호출 방식
async def allad(request:Request):
    return templates.TemplateResponse(name="offerwall/allad.html", context={'request':request})

# 광고 하나를 클릭했을 때 : 주소 /clicktech/alllist/detail
@router.get("/alllist/detail") # 펑션 호출 방식
async def allad(request:Request):
    return templates.TemplateResponse(name="offerwall/allad_detail.html", context={'request':request})


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
    return templates.TemplateResponse(name="notice/notice_detail.html", context={'request':request})

# FAQ 클릭했을 때 : 주소 /clicktech/faq
@router.get("/faq") # 펑션 호출 방식
async def faq(request:Request):
    return templates.TemplateResponse(name="faq/faq_main.html", context={'request':request})

# FAQ의 글 하나를 클릭했을 때 : 주소 /clicktech/faq
@router.get("/faq/detail") # 펑션 호출 방식
async def faq(request:Request):
    return templates.TemplateResponse(name="faq/faq_detail.html", context={'request':request})
