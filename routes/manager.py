from fastapi import APIRouter
from starlette.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from databasess.connections import Database
from typing import Optional
from routes.paginations import Paginations
from databasess.mongo_connect import User_info, Gifty_info, Notice, Faq, Ad_main, Ad_create
from beanie import PydanticObjectId

collection_ad_create = Database(Ad_create)
collection_faq = Database(Faq)
collection_notice = Database(Notice)
collection_user = Database(User_info)


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
    try :
        if user_dict['key'] == "type" :
            if user_dict['word'] == "download_app" : user_dict['word'] ="앱 설치"
            elif  user_dict['word'] =="join"  :user_dict['word'] = "회원가입"
            elif user_dict['word'] == "newsletter": user_dict['word'] = "뉴스레터 구독"
            elif user_dict['word'] =="enter" : user_dict['word'] = "사이트 접속"
            elif user_dict['word'] == "purchase" : user_dict['word'] = "구매"
    except :
        pass
    
    return templates.TemplateResponse(name="manager/ad_list.html", context={'request':request,
                                                                            'ad_list':ad_list,
                                                                            'pagination':pagination,
                                                                             "user_dict":user_dict})
@router.get("/adlist/{page_number}") # 펑션 호출 방식
@router.post("/adlist")
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
        if user_dict['key'] == "type" :
                if user_dict['word'] == "download_app" : user_dict['word'] ="앱 설치"
                elif  user_dict['word'] =="join"  :user_dict['word'] = "회원가입"
                elif user_dict['word'] == "newsletter": user_dict['word'] = "뉴스레터 구독"
                elif user_dict['word'] =="enter" : user_dict['word'] = "사이트 접속"
                elif user_dict['word'] == "purchase" : user_dict['word'] = "구매"
    except :
        pagination=1
        ad_list = await collection_ad_create.get_all()
    return templates.TemplateResponse(name="manager/ad_list.html", context={'request':request,
                                                                            'ad_list':ad_list,
                                                                            'pagination':pagination,
                                                                             "user_dict":user_dict})
# FAQ 생성/관리에서 생성 클릭했을 때 : 주소 /manager/faq/delete/object_id
@router.get("/ad/delete/{object_id}")
async def delete_review(request: Request, object_id:PydanticObjectId):
    await collection_ad_create.delete_one(object_id)
    return templates.TemplateResponse(name="manager/ad_delete.html", context={'request':request})

# 광고 생성 클릭했을 때 : 주소 /manager/ad
@router.post("/ad/submit") # 펑션 호출 방식
async def ad(request:Request):
    ad_dict = dict(await request.form())
    ad_info = Ad_create(**ad_dict)
    await collection_ad_create.save(ad_info)

    return templates.TemplateResponse(name="manager/ad_create.html", context={'request':request})

#-----------------------FAQ 부분임당------------------------#

# FAQ 생성/관리 클릭했을 때 : 주소 /manager/faq

@router.get("/faq/{page_number}")
@router.get("/faq") # 펑션 호출 방식
async def listfaq_get(request:Request, page_number: Optional[int] = 1):
    user_dict = dict(await request.form())
    list_faq = await collection_faq.get_all()
    try : 
        user_dict = dict(request._query_params)
        conditions = { user_dict['key'] : { '$regex': user_dict["word"] } }
    except :
        conditions = { }
    list_faq, pagination = await collection_faq.getsbyconditionswithpagination(conditions, page_number)
    return templates.TemplateResponse(name="manager/faq_list.html", context={'request':request,
                                                                             'list_faq':list_faq,
                                                                             'pagination':pagination,
                                                                             "user_dict":user_dict})
# FAQ 생성 후 완료 클릭했을 때(post방식) : 주소 /manager/faq
@router.get("/faq/{page_number}")
@router.post("/faq") # 펑션 호출 방식
async def listfaq_post(request:Request, page_number: Optional[int] = 1):
    user_dict = dict(await request.form())
    faq = Faq(**user_dict)
    await collection_faq.save(faq)
    list_faq = await collection_faq.get_all()
    try : 
        user_dict = dict(request._query_params)
        conditions = { user_dict['key'] : { '$regex': user_dict["word"] } }
    except :
        conditions = { }
    list_faq, pagination = await collection_faq.getsbyconditionswithpagination(conditions, page_number)
    
    return templates.TemplateResponse(name="manager/faq_list.html", context={'request':request,
                                                                             'list_faq':list_faq,
                                                                             'pagination':pagination,
                                                                             "user_dict":user_dict})
# FAQ 생성/관리에서 생성 클릭했을 때 : 주소 /manager/faq/delete/object_id
@router.get("/faq/delete/{object_id}")
async def delete_review(request: Request, object_id:PydanticObjectId):
    await collection_faq.delete_one(object_id)
    return templates.TemplateResponse(name="manager/faq_delete.html", context={'request':request})


# FAQ 생성/관리에서 생성 클릭했을 때 : 주소 /manager/faq/create
@router.post("/faq/create") # 펑션 호출 방식
async def createfaq(request:Request):
    return templates.TemplateResponse(name="manager/faq_create.html", context={'request':request})

# -------------------------------공지사항부분임당 ------------------------------------------#
# 공지사항 생성/관리 클릭했을 때 : 주소 /manager/notice

@router.get("/notice/{page_number}")
@router.get("/notice") # 펑션 호출 방식
async def listfaq_get(request:Request, page_number: Optional[int] = 1):
    user_dict = dict(await request.form())
    list_notice = await collection_notice.get_all()
    try : 
        user_dict = dict(request._query_params)
        conditions = { user_dict['key'] : { '$regex': user_dict["word"] } }
    except :
        conditions = { }
    list_notice, pagination = await collection_notice.getsbyconditionswithpagination(conditions, page_number)
    
    return templates.TemplateResponse(name="manager/notice_list.html", context={'request':request,
                                                                             'list_notice':list_notice,
                                                                             'pagination':pagination,
                                                                             "user_dict":user_dict})
# 공지사항 생성 후 완료 클릭했을 때(post방식) : 주소 /manager/faq
@router.get("/notice/{page_number}")
@router.post("/notice") # 펑션 호출 방식
async def listfaq_post(request:Request, page_number: Optional[int] = 1):
    user_dict = dict(await request.form())
    notice = Notice(**user_dict)
    await collection_notice.save(notice)
    list_notice = await collection_notice.get_all()
    try : 
        user_dict = dict(request._query_params)
        conditions = { user_dict['key'] : { '$regex': user_dict["word"] } }
    except :
        conditions = { }
    list_notice, pagination = await collection_notice.getsbyconditionswithpagination(conditions, page_number)
    return templates.TemplateResponse(name="manager/notice_list.html", context={'request':request,
                                                                             'list_notice':list_notice,
                                                                             'pagination':pagination,
                                                                             "user_dict":user_dict})
# 공지사항 생성/관리에서 생성 클릭했을 때 : 주소 /manager/faq/delete/object_id
@router.get("/notice/delete/{object_id}")
async def delete_review(request: Request, object_id:PydanticObjectId):
    await collection_notice.delete_one(object_id)
    return templates.TemplateResponse(name="manager/notice_delete.html", context={'request':request})

# 공지사항 생성/관리에서 생성 클릭했을 때 : 주소 /manager/faq/create
@router.post("/notice/create") # 펑션 호출 방식
async def createfaq(request:Request):
    return templates.TemplateResponse(name="manager/notice_create.html", context={'request':request})




# 관리자 계정 관리 클릭했을 때 : 주소 /manager/manager_account
@router.get("/manager_account") # 펑션 호출 방식
async def manager(request:Request):
    return templates.TemplateResponse(name="manager/manageraccount.html", context={'request':request})



@router.get("/user_account/{page_number}") # 펑션 호출 방식
@router.get("/user_account")
async def get_user_account(request:Request, page_number: Optional[int] = 1):
    user_dict = dict(await request.form())
    user_list = await collection_user.get_all()
    conditions = { }
    try :
        if user_dict['key'] == "type" :
            if user_dict['word'] == "이름" : user_dict['word'] ="user_name"
            elif  user_dict['word'] == "아이디" :user_dict['word'] ="user_id" 
            elif user_dict['word'] == "이메일": user_dict['word'] ="user_email"    
        conditions = { user_dict['key'] : { '$regex': user_dict["word"] } }
    except :
        conditions = { }
    user_list, pagination = await collection_user.getsbyconditionswithpagination(conditions, page_number)
    try :
        if user_dict['key'] == "type" :
            if user_dict['word'] == "user_name" : user_dict['word'] ="이름"
            elif  user_dict['word'] =="user_id"  :user_dict['word'] = "아이디"
            elif user_dict['word'] == "user_email": user_dict['word'] = "이메일"
    except :
        pass
        pagination=1
        user_list = await collection_ad_create.get_all()
    user_list, pagination = await collection_user.getsbyconditionswithpagination(conditions, page_number)
    return templates.TemplateResponse(name="manager/useraccount.html", context={'request':request,
                                                                            'user_list':user_list,
                                                                            'pagination':pagination,
                                                                             "user_dict":user_dict})
@router.get("/user_account/delete/{object_id}")
async def delete_user_account(request: Request, object_id:PydanticObjectId):
    await collection_user.delete_one(object_id)
    return templates.TemplateResponse(name="manager/useraccount_delete.html", context={'request':request})