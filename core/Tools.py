"""
@File  : Tools.py
@Author: djw
@CreateDate  : 2022/11/8 15:20:30
@Description  : 提供一些功能的工具函数和类
"""
from datetime import datetime
from datetime import timedelta


def get_time_range(days):
    """获取从几天前的时间点"""
    times = datetime.now() + timedelta(days=-days)
    return times.strftime('%Y-%m-%d %H:%M:%S')
