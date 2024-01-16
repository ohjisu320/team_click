from fastapi import FastAPI, APIRouter, Request, Form
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from databases.connections import Database
from models.user_info import User_info
from models.faq import Faq
from routes.paginations import Paginations
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

from models.ad_create import Ad_create
collection_ad_create = Database(Ad_create)
# 전체리스트 클릭했을 때 : 주소 /clicktech/alllist
@router.get("/alllist/") # 펑션 호출 방식
async def allad(request:Request):
    ad_list = await collection_ad_create.get_all()
    return templates.TemplateResponse(name="offerwall/allad.html", context={'request':request,
                                                                            "ad_list":ad_list})

@router.get("/alllist/{type}") # 펑션 호출 방식
async def allad(request:Request, type):
    conditions = {'type': { '$regex': type }}
    ad_list = await collection_ad_create.getsbyconditions(conditions)
    return templates.TemplateResponse(name="offerwall/allad.html", context={'request':request,
                                                                            "ad_list":ad_list})

# 광고 하나를 클릭했을 때 : 주소 /clicktech/alllist/detail
@router.get("/alllist/detail/{object_id}") # 펑션 호출 방식
async def detailad(request:Request, object_id):
    ad_detail = await collection_ad_create.get(object_id)
    return templates.TemplateResponse(name="offerwall/allad_detail.html", context={'request':request,
                                                                                   "ad_detail":ad_detail})

from models.gifty_info import Gifty_info
collection_gifty = Database(Gifty_info)
# 쿠폰교환 클릭했을 때 : 주소 /clicktech/exchange
@router.get("/exchange") # 펑션 호출 방식
async def exchange(request:Request):
    gifty_list = await collection_gifty.get_all()
    return templates.TemplateResponse(name="exchange/gifticon_main.html", context={'request':request,
                                                                                   "gifty_list" : gifty_list})

@router.get("/exchange/{gifty_style}") # 펑션 호출 방식
async def exchange(request:Request, gifty_style):
    if gifty_style =="cafe" : gifty_style ="카페"
    if gifty_style =="bake" : gifty_style ="베이커리/도넛/떡"
    if gifty_style =="mart" : gifty_style ="백화점/마트"
    if gifty_style =="icecream" : gifty_style ="아이스크림"
    if gifty_style =="convin" : gifty_style ="편의점"
    if gifty_style =="burger" : gifty_style ="버거/피자"
    if gifty_style =="chicken" : gifty_style ="치킨"
    if gifty_style =="korean" : gifty_style ="한식/중식/분식"
    if gifty_style =="jokbal" : gifty_style ="구이/족발"
    if gifty_style =="restaurant" : gifty_style ="레스토랑/뷔페"
    if gifty_style =="fusion" : gifty_style ="외국/퓨전/기타"
    if gifty_style =="movie" : gifty_style ="영화/음악/도서"
    if gifty_style =="commu" : gifty_style ="kt/통신"
    if gifty_style =="beauty" : gifty_style ="뷰티/헤어/바디"
    if gifty_style =="health" : gifty_style ="건강/리빙/식품관"
    if gifty_style =="enter" : gifty_style ="생활/가전/엔터"
    condition = {'gifty_style':{'$regex':gifty_style}}
    gifty_list = await collection_gifty.getsbyconditions(condition)
    return templates.TemplateResponse(name="exchange/gifticon_main.html", context={'request':request,
                                                                                   "gifty_list" : gifty_list})

# 쿠폰교환페이지에서 쿠폰 하나를 클릭했을 때 : 주소 /clicktech/exchange/detail
@router.get("/exchange/detail/{object_id}") # 펑션 호출 방식
async def exchange(request:Request, object_id):
    condition = {'_id' : {'$regex' : object_id}}
    gifty_list = await collection_gifty.getsbyconditions(condition)
    return templates.TemplateResponse(name="exchange/gifticon_detail.html", context={'request':request,
                                                                                     "gifty_list": gifty_list})

# 공지사항 클릭했을 때 : 주소 /clicktech/notice
@router.get("/notice") # 펑션 호출 방식
async def notice(request:Request):
    return templates.TemplateResponse(name="notice/notice_main.html", context={'request':request})

# 공지사항의 글 하나를 클릭했을 때 : 주소 /clicktech/notice/detail
@router.get("/notice/detail") # 펑션 호출 방식
async def notice(request:Request):
    return templates.TemplateResponse(name="notice/notice_detail.html", context={'request':request})

from typing import Optional
# # FAQ 클릭했을 때 : 주소 /clicktech/faq
collection_faq = Database(Faq)
@router.get("/faq") # 펑션 호출 방식
async def faq(request:Request,page_number: Optional[int] = 1):
    await request.form()
    list_faq = await collection_faq.get_all()
    total = len(list_faq)
    pagination = Paginations(total,page_number)
    conditions = { }
    list_faq_pagination, pagination = await collection_faq.getsbyconditionswithpagination(page_number,conditions)
    return templates.TemplateResponse(name="faq/faq_main.html", context={'request':request,
                                                                         'list_faq' : list_faq_pagination,
                                                                         'pagination': pagination })

@router.get("/faq/{categories}") # 펑션 호출 방식
async def faq_list(request:Request,categories, page_number: Optional[int] = 1):
    await request.form()
    cate_list_faq = await collection_faq.get(categories)
    total = len(cate_list_faq)
    pagination = Paginations(total,page_number)
    conditions = { }
    list_faq_pagination,pagination = await collection_faq.getsbyconditionswithpagination(conditions,page_number)
    return templates.TemplateResponse(name="faq/faq_main.html", context={'request':request,
                                                                            'list_faq' : list_faq_pagination,
                                                                          'pagination': pagination })

# @router.get("/faq/{categories}")
# @router.get("/faq")
# async def faq_list(request:Request,categories, page_number: Optional[int] = 1):
#     # await request.form()
#     list_faq = await collection_faq.get_all()
    
#     print(list_faq)
#     conditions = { }
#     try :
#         search_word = list_faq["categories"]
#     except:
#         search_word = None
#     if search_word:     # 검색어 작성
#         conditions = {'categories' : { '$regex': categories }}
#     # db.answers.find({'name':{ '$regex': '김' }})
#     # { 'name': { '$regex': user_dict.word } }
#     list_faq, pagination = await collection_faq.getsbyconditionswithpagination(conditions
#                                                                      ,page_number)
#     return templates.TemplateResponse(name="faq/faq_main.html"
#                                       , context={'request':request,
#                                                  'list_faq' : list_faq,
#                                                 'pagination': pagination })
