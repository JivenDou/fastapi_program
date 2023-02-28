# -*- coding:utf-8 -*-
"""
@Time : 2023/2/25 10:15 AM
@Author: djw
@Des: redis数据库
"""

import aioredis
from aioredis import Redis
from config import settings


async def sys_cache() -> Redis:
    """
    系统缓存
    :return: cache 连接池
    """
    # 从URL方式创建redis连接池
    sys_cache_pool = aioredis.ConnectionPool.from_url(
        f"redis://{settings.REDIS_HOST}:{settings.REDIS_POST}",
        db=0,   # 使用第0个redis数据库
        encoding='utf-8',
        decode_responses=True
    )
    return Redis(connection_pool=sys_cache_pool)


# async def code_cache() -> Redis:
#     """
#     系统缓存
#     :return: cache 连接池
#     """
#     # 从URL方式创建redis连接池
#     sys_cache_pool = aioredis.ConnectionPool.from_url(
#         f"redis://{settings.REDIS_HOST}:{settings.REDIS_POST}",
#         db=1,   # 使用第1个redis数据库
#         encoding='utf-8',
#         decode_responses=True
#     )
#     return Redis(connection_pool=sys_cache_pool)
