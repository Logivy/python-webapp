from json import encoder
import logging                  # 日志模块

from aiohttp import web
import aiohttp
import asyncio

logging.basicConfig(level=logging.INFO)                             # 日志格式

# 请求处理程序，返回响应
async def handelHello(request):
    return web.Response(body="<h1>Hello World!</h1>".encode('utf-8'),content_type='text/html')

def init():
    app = web.Application()                                         # 创建一个应用程序（web服务器）
    app.add_routes([web.get(path='/',handler=handelHello)])         # 分配路由
    web.run_app(app,host="127.0.0.1",port=8080)                     # 运行web服务器
    logging.info('server started at http://127.0.0.1:8080...')

init()


# def index(request):
#     return web.Response(body='<h1>AWesome</h1>'.encode('utf-8'), content_type='text/html')


# def init():
#     app = web.Application()
#     app.router.add_route('GET', '/', index)
#     web.run_app(app, host='127.0.0.1', port=8080)
#     logging.info('server started at http://127.0.0.1:8080...')


# init()
