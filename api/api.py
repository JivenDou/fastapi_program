from fastapi import APIRouter
from api.endpoints import login

api_router = APIRouter()
api_router.include_router(login.router, prefix='/User', tags=["用户登录页"])
