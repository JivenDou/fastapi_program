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


# =============================常用配置=============================
class Config(BaseSettings):
    """常用配置信息"""
    # 调试模式
    APP_DEBUG: bool = False     # 若设置True，则显示调试信息
    # 接口ip和端口
    API_IP: str = "0.0.0.0"     # fastapi接口ip
    API_PORT: int = 8045        # fastapi接口端口
    RELOAD: bool = False
    # 项目信息
    VERSION: str = "0.0.1"  # 版本号
    PROJECT_NAME: str = "XXXX系统接口文档"    # 接口文档名
    DESCRIPTION: str = '<a href="" target="_blank">好好工作！努力赚钱！！</a>'     # 备注/链接
    # 静态资源目录
    STATIC_DIR: str = os.path.join(os.getcwd(), "static")
    TEMPLATE_DIR: str = os.path.join(STATIC_DIR, "templates")
    # 跨域请求
    CORS_ORIGINS: List = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List = ["*"]
    CORS_ALLOW_HEADERS: List = ["*"]


settings = Config()
# =============================数据库配置=============================
DB_ORM_CONFIG = {
    "connections": {
        # 链接第一个数据库
        "db1": {
            'engine': 'tortoise.backends.mysql',    # 默认不改
            "credentials": {
                'host': "127.0.0.1",            # 数据库ip
                'user': "root",                 # 数据库用户名
                'password': "zzZZ4144670..",    # 数据库密码
                'port': 3306,                   # 数据库端口
                'database': "test",             # 数据库名
            }
        },
        # 链接第二个数据库
        # "db2": {
        #     'engine': 'tortoise.backends.mysql',
        #     "credentials": {
        #         'host': "127.0.0.1",
        #         'user': "root",
        #         'password': "zzZZ4144670..",
        #         'port': 3306,
        #         'database': "shucai",
        #     }
        # },
    },
    "apps": {
        "db1": {
            "models": [],  # 自动生成表模型路径（可不填）
            "default_connection": "db1"     # 上面链接的数据库键名
        },
        # "db2": {
        #     "models": ["database.models.db1"],
        #     "default_connection": "db2"
        # },
    },
    'use_tz': False,
    'timezone': 'Asia/Shanghai'     # 设置时区
}
