'''
# @Author       : Chr_
# @Date         : 2021-03-16 20:58:43
# @LastEditors  : Chr_
# @LastEditTime : 2022-07-16 08:24:26
# @Description  : 响应模型
'''

from typing import Dict, List
from pydantic import BaseModel
from .posts import Posts_Out


class BaseResponse(BaseModel):
    '''
    普通响应模型
    '''
    code: int = 0
    msg: str = ''


class PostsListResponse(BaseResponse):
    '''
    列表响应模型
    '''
    count: int = 0
    data:  List[Posts_Out] = []


class PostDetailResponse(BaseResponse):
    '''
    详情响应模型
    '''
    data:  Posts_Out = None


class PostIdsResponse(BaseResponse):
    '''
    响应模型
    '''
    count: int = 0
    data:  List[str] = None
