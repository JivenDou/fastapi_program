# -*- coding:utf-8 -*-
"""
@Time : 2023/2/28 10:11 AM
@Author: djw
@Des: 常用返回类型封装
"""


def base_response(code, msg, data=None):
    """基础返回格式"""
    if data is None:
        data = []
    result = {
        "code": code,
        "message": msg,
        "data": data
    }
    return result


def success(msg='', data=None):
    """成功返回格式"""
    return base_response(200, msg, data)


def fail(msg='', data=None, code=-1):
    """失败返回格式"""
    return base_response(code, msg, data)
