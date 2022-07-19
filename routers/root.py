'''
# @Author       : Chr_
# @Date         : 2021-03-15 20:30:14
# @LastEditors  : Chr_
# @LastEditTime : 2022-07-19 08:35:35
# @Description  : 首页路由
'''

from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter(prefix='',
                   tags=['根'],
                   responses={404: {'detail': 'page not found'}},)


@router.get('/', response_class=RedirectResponse)
async def index():
    return "/index.html"
