# -*- coding:utf-8 -*-
"""
@Created on : 2022/4/22 22:02
@Author: binkuolo
@Des: fastapi事件监听
"""

from typing import Callable
from fastapi import FastAPI
from database.mysql import register_mysql
from database.redis import sys_cache
from aioredis import Redis


def startup(app: FastAPI) -> Callable:
    """
    FastApi 启动完成事件
    :param app: FastAPI
    :return: start_app
    """
    async def app_start() -> None:
        # APP启动完成后触发
        print("==================FastApi已启动==================")
        # 注册mysql数据库
        await register_mysql(app)
        print("---------mysql数据库连接成功---------")
        # 注入连接池到app state
        app.state.cache = await sys_cache()
        # app.state.code_cache = await code_cache()
        print("---------redis连接池创建成功---------")
    return app_start


def stopping(app: FastAPI) -> Callable:
    """
    FastApi 停止事件
    :param app: FastAPI
    :return: stop_app
    """
    async def app_stop() -> None:
        # APP停止时触发
        cache: Redis = await app.state.cache
        # code: Redis = await app.state.code_cache
        await cache.close()
        # await code.close()
        # print("---------redis连接池已关闭---------")
        print("==================FastApi已停止==================")
    return app_stop
