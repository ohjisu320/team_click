from fastapi import FastAPI, APIRouter, Request, Form
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from databases.connections import Database
from models.user_info import User_info
from models.faq import Faq
router = APIRouter()
app = FastAPI()
collection_user = Database(User_info)

templates = Jinja2Templates(directory="templates/")
from databases.connections import Database
from models.ad_main import Ad_main
collection_ad_main = Database(Ad_main)
# 로고 클릭했을 때 : 주소 /clicktech/
@router.get("/") # 펑션 호출 방식
async def usermain(request:Request):
    ad_main = await collection_ad_main.get_all()
    return templates.TemplateResponse(name="usermain.html", context={'request':request,
                                                                     'ad_main':ad_main})

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

@router.post("/join/step3")
async def read_item(request: Request, user_terms1: str = Form('off'), user_terms2: str = Form('off'), user_terms3: str = Form('off'), user_terms4: str = Form('off')):
    return templates.TemplateResponse(name="join/step3.html",context={"request": request, "user_terms1": user_terms1 == 'on', "user_terms2": user_terms2 == 'on', "user_terms3": user_terms3 == 'on', "user_terms4": user_terms4 == 'on'})

app.include_router(router)

# database 의 connections에 정의된 Database 클래스와 user_info collection을 정의한 User_info 클래스를 import

from models.user_info import User_info
collection_user = Database(User_info)
@router.post("/join/step4") # 펑션 호출 방식
async def user_input_post(request:Request):
    user_dict = dict(await request.form())
    try:
        user_dict['user_terms1'] = user_dict.get('user_terms1', 'off')
        user_dict['user_terms2'] = user_dict.get('user_terms2', 'off')
        user_dict['user_terms3'] = user_dict.get('user_terms3', 'off')
        user_dict['user_terms4'] = user_dict.get('user_terms4', 'off')
        user = User_info(**user_dict)
        await collection_user.save(user)
    except Exception as e:
        print(f"Error occurred: {e}") # 키 값에 해당되는 input이 없으면 빈 값이 주어지도록 설정
        user = User_info(user_terms1="on", user_terms2="on", user_terms3="off", user_terms4="off")
        await collection_user.save(user)
    # 리스트 정보
    user_list = await collection_user.get_all()
    return templates.TemplateResponse(name="join/step4.html"
                                      , context={'request':request, "user_info":user_list})

# # Sign-in 클릭했을 때 : 주소 /clicktech/join
# @router.get("/join/step4") # 펑션 호출 방식
# async def join(request:Request):
#     return templates.TemplateResponse(name="join/step4.html", context={'request':request})

from models.ad_alllist import Ad_alllist
collection_ad_alllist = Database(Ad_alllist)
# 전체리스트 클릭했을 때 : 주소 /clicktech/alllist
@router.get("/alllist") # 펑션 호출 방식
async def allad(request:Request):
    ad_list = await collection_ad_alllist.get_all()
    print(ad_list)
    return templates.TemplateResponse(name="offerwall/allad.html", context={'request':request,
                                                                            "ad_list":ad_list})

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



database_faq = Database(Faq)
from typing import Optional
@router.get("/faq")
@router.get("/faq/{page_number}")
async def faq_list(request:Request, page_number: Optional[int] = 1):
    list_faq = dict(request._query_params)
    print(list_faq)
    # db.answers.find({'name':{ '$regex': '김' }})
    # { 'name': { '$regex': user_dict.word } }
    conditions = { }
    try :
        search_word = list_faq["word"]
    except:
        search_word = None
    if search_word:     # 검색어 작성
        conditions = {list_faq['categories'] : { '$regex': list_faq["word"] }}
    
    list_faq, pagination = await database_faq.getsbyconditionswithpagination(conditions
                                                                     ,page_number)
    return templates.TemplateResponse(name="faq/faq_main.html"
                                      , context={'request':request
                                                 , 'faqs' : list_faq
                                                  ,'pagination' : pagination })