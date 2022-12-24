from aiohttp import web


async def index(request: web.Request) -> web.Response:
    return web.Response(text="Index page.")


async def health(request: web.Request) -> web.Response:
    return web.Response(text="Ok", status=200)
