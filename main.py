
'''
# @Author       : Chr_
# @Date         : 2021-03-09 15:46:46
# @LastEditors  : Chr_
# @LastEditTime : 2022-07-19 10:13:55
# @Description  : 启动入口
'''

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from tortoise.contrib.fastapi import register_tortoise

from routers import posts, root

app = FastAPI(
    title='后端',
    description='普普通通的后端',
    version='1.0',
    jinja2=False
)


app.include_router(root.router)
app.include_router(posts.router)

app.mount('/', StaticFiles(directory='static'), name='静态文件')

register_tortoise(
    app,
    db_url='sqlite://data.db',
    modules={
        'models': [
            'models.posts',
        ]
    },
    generate_schemas=True,
    add_exception_handlers=True,
)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
