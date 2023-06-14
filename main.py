"""
@File  : main.py
@Author: djw
@CreateDate  : 2022/11/4 15:20
@UpdateDate  : 2022/11/28 10:33
@Description  : 此文件为程序运行文件
"""
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.openapi.docs import (get_redoc_html, get_swagger_ui_html)
from core import Router, Events
from config import settings

app = FastAPI(title=settings.PROJECT_NAME,
              description=settings.DESCRIPTION,
              version=settings.VERSION,
              debug=settings.APP_DEBUG,
              docs_url=None,
              redoc_url=None)

# 配置允许域名列表、允许方法、请求头、cookie等
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)


# # 重写 swagger_ui 接口文档设置，使文档能够在局域网访问
# @app.get("/docs", include_in_schema=False)
# async def custom_swagger_ui_html():
#     return get_swagger_ui_html(
#         openapi_url=app.openapi_url,
#         title=app.title + " - Swagger UI",
#         oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
#         swagger_js_url="/swagger-ui-bundle.js",
#         swagger_css_url="/swagger-ui.css",
#     )
#
#
# # 重写 redoc 接口文档设置，使文档能够在局域网访问
# @app.get("/redoc", include_in_schema=False)
# async def redoc_html():
#     return get_redoc_html(
#         openapi_url=app.openapi_url,
#         title=app.title + " - ReDoc",
#         redoc_js_url="/redoc.standalone.js",
#     )

# 事件监听
app.add_event_handler("startup", Events.startup(app))       # fastapi启动时触发，包含注册数据库、redis等操作
app.add_event_handler("shutdown", Events.stopping(app))     # fastapi关闭时触发
# 路由
app.include_router(Router.router)   # 包含各个路由
# 设置静态资源目录
# app.mount('/', StaticFiles(directory=settings.STATIC_DIR), name="static")
# app.state.views = Jinja2Templates(directory=settings.TEMPLATE_DIR)

if __name__ == '__main__':
    uvicorn.run(
        app=app,
        host=settings.API_IP,
        port=settings.API_PORT,
        reload=settings.RELOAD
    )
