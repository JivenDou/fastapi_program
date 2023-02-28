from fastapi import APIRouter, Request
from schemas.endpoints import login
from tortoise import Tortoise

router = APIRouter()


@router.post("/Login", summary="验证登录信息")
async def verify_login(item: login.LoginInfo, req: Request):
    """
    请求参数说明：
    - "userName"：用户名（类型：str）
    - "password"：密码（类型：str）
    """
    # 链接数据库
    db = Tortoise.get_connection("db1")
    user_name = item.userName
    password = item.password

    # 设置redis键值，超时时间为60秒
    await req.app.state.cache.set(name="name", value='djw', ex=60)
    # 获取redis键值
    name = await req.app.state.cache.get(name="name")
    print(name)

    sql = f"SELECT * FROM user WHERE username = '{user_name}' AND password = '{password}'"
    # 执行数据库语句
    result = await db.execute_query_dict(sql)
    if result:
        return {"msg": "success"}
    else:
        return {"msg": "error"}
