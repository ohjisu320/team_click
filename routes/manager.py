from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from databases.mongo_connect import Ad_create
from databases.connections import Database
from typing import Optional
from routes.paginations import Paginations
collection_ad_create = Database(Ad_create)


router = APIRouter()

templates = Jinja2Templates(directory="templates/")

# 로고 클릭했을 때 : 주소 /manager/
@router.get("/") # 펑션 호출 방식
async def usermain(request:Request):
    return templates.TemplateResponse(name="manager/manager_main.html", context={'request':request})

# 회원관리 클릭했을 때 : 주소 /manager/user
@router.get("/user") # 펑션 호출 방식
async def user(request:Request):
    return templates.TemplateResponse(name="manager/user_manage.html", context={'request':request})


# 포인트 통계 클릭했을 때 : 주소 /manager/point
@router.get("/point") # 펑션 호출 방식
async def point(request:Request):
    return templates.TemplateResponse(name="manager/point_data.html", context={'request':request})

# 광고 생성 클릭했을 때 : 주소 /manager/ad
@router.get("/ad") # 펑션 호출 방식
async def ad(request:Request):
    return templates.TemplateResponse(name="manager/ad_manage.html", context={'request':request})


# 광고 리스트 클릭했을 때 : 주소 /manager/adlist
@router.get("/adlist/{page_number}") # 펑션 호출 방식
@router.get("/adlist")
async def ad(request:Request, page_number: Optional[int] = 1):
    try : 
        user_dict = dict(request._query_params)
        ad_list = await collection_ad_create.get_all()
        conditions = { }
        # total = len(ad_list)
        # pagination = Paginations(total,page_number)
        try :
            if user_dict['key'] == "type" :
                if user_dict['word'] == "앱 설치" : user_dict['word'] ="download_app"
                elif  user_dict['word'] == "회원가입" :user_dict['word'] ="join" 
                elif user_dict['word'] == "뉴스레터 구독": user_dict['word'] ="newsletter"    
                elif user_dict['word'] =="사이트 접속": user_dict['word'] = "enter" 
                elif user_dict['word'] == "구매" : user_dict['word'] ="purchase"
            conditions = { user_dict['key'] : { '$regex': user_dict["word"] } }
        except :
            conditions = { }
        ad_list, pagination = await collection_ad_create.getsbyconditionswithpagination(conditions, page_number)
    except :
        pagination=1
        ad_list = await collection_ad_create.get_all()
    return templates.TemplateResponse(name="manager/ad_list.html", context={'request':request,
                                                                            'ad_list':ad_list,
                                                                            'pagination':pagination})




# 광고 생성 클릭했을 때 : 주소 /manager/ad
@router.post("/ad/submit") # 펑션 호출 방식
async def ad(request:Request):
    ad_dict = dict(await request.form())
    ad_info = Ad_create(**ad_dict)
    await collection_ad_create.save(ad_info)

    return templates.TemplateResponse(name="manager/ad_create.html", context={'request':request})


# 관리자 관리 클릭했을 때 : 주소 /manager/manager
@router.get("/manager") # 펑션 호출 방식
async def manager(request:Request):
    return templates.TemplateResponse(name="manager/manager_manage.html", context={'request':request})


