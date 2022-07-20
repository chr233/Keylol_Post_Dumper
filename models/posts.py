'''
# @Author       : Chr_
# @Date         : 2021-03-16 18:22:12
# @LastEditors  : Chr_
# @LastEditTime : 2022-07-20 12:32:38
# @Description  : 用户数据库模型
'''

from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Posts(models.Model):
    '''
    帖子模型
    '''
    id = fields.IntField(pk=True, index=True)
    tid = fields.CharField(unique=True, max_length=255, description='帖子tid')
    post_url = fields.CharField(max_length=255, description='帖子链接')
    post_title = fields.CharField(max_length=255, description='帖子标题')
    author_nick = fields.TextField(default='', description='作者昵称')
    author_uid = fields.TextField(default='', description='作者uid')
    post_date = fields.CharField(max_length=50, description='帖子发布时间')
    content = fields.TextField(default='', description='帖子内容')
    game_list = fields.TextField(default='', description='游戏列表')
    game_bbcode = fields.TextField(default='', description='游戏列表2')
    game_excel = fields.TextField(default='', description='游戏列表3')

    def __str__(self) -> str:
        return self.post_title

    class Meta:
        table_description = "帖子数据"
        indexes = ["tid", "post_title"]


Posts_In = pydantic_model_creator(
    Posts, name='posts_in', exclude=('id',)
)

Posts_Out = pydantic_model_creator(
    Posts, name='post_out',
)
