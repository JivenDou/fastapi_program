from pydantic import BaseModel


class LoginInfo(BaseModel):
    """验证登录信息"""
    userName: str = "djw"
    password: str = "123456"
