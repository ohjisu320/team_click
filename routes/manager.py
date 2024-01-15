from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

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

# 광고 관리 클릭했을 때 : 주소 /manager/ad
@router.get("/ad") # 펑션 호출 방식
async def ad(request:Request):
    return templates.TemplateResponse(name="manager/ad_manage.html", context={'request':request})

# 관리자 관리 클릭했을 때 : 주소 /manager/manager
@router.get("/manager") # 펑션 호출 방식
async def manager(request:Request):
    return templates.TemplateResponse(name="manager/manager_manage.html", context={'request':request})


