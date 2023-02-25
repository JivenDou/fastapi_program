"""
@File  : config.py
@Author: djw
@CreateDate  : 2022/11/4 15:20
@UpdateDate  : 2022/11/28 10:33
@Description  : 此文件为配置文件（修改此文件即可）
"""
import os
from pydantic import BaseSettings
from typing import List


class Config(BaseSettings):
    # 调试模式
    APP_DEBUG: bool = False
    # 接口ip和端口
    API_IP: str = "0.0.0.0"
    API_PORT: int = 8045
    RELOAD: bool = False
    # 数据库连接
    DB_USERNAME: str = "root"
    DB_PASSWORD: str = "zzZZ4144670.."
    DB_IP: str = "127.0.0.1"
    DB_PORT: str = "3306"
    DATABASE: str = "centralized_control_guangfu"
    # 项目信息
    VERSION: str = "0.0.1"
    PROJECT_NAME: str = "XXXX系统接口文档"
    DESCRIPTION: str = '<a href="" target="_blank">好好工作！努力赚钱！！</a>'
    # 静态资源目录
    STATIC_DIR: str = os.path.join(os.getcwd(), "static")
    TEMPLATE_DIR: str = os.path.join(STATIC_DIR, "templates")
    # 跨域请求
    CORS_ORIGINS: List = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List = ["*"]
    CORS_ALLOW_HEADERS: List = ["*"]


settings = Config()
