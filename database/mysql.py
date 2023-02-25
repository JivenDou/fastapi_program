# -*- coding:utf-8 -*-
"""
@Time : 2023/2/25 10:15 AM
@Author: djw
@Des: mysql数据库
"""

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from config import DB_ORM_CONFIG

async def register_mysql(app: FastAPI):
    # 注册数据库
    register_tortoise(
        app,
        config=DB_ORM_CONFIG,
        generate_schemas=True,
        add_exception_handlers=True,
    )
