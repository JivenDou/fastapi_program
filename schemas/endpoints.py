"""
@Time : 2023/3/1 1:46 PM
@Author: djw
@Des: 关于主要接口的所有请求体模板
"""
from pydantic import BaseModel, Field


class LoginInfo(BaseModel):
    """验证登录信息"""
    userName: str = Field(min_length=3, max_length=10, description="用户名", default="djw")
    password: str = Field(min_length=6, max_length=12, description="密码", default="123456")
