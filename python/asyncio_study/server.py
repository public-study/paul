import asyncio
import random

from aiohttp import web
from aiohttp.web_request import Request


async def echo_name(request: Request):
    await asyncio.sleep(random.randint(0, 5))
    name = request.match_info.get("name", "Anonymous")
    return web.json_response({"hi": name})


async def index(request: Request):
    await asyncio.sleep(random.randint(0, 5))
    return web.json_response({"index": "page"})


app = web.Application()
app.add_routes([
    web.get("/", index),
    web.get("/{name}", echo_name)
])

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0")
