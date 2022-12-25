import logging

from aiohttp import web

logger = logging.getLogger(__name__)


async def index(request: web.Request) -> web.Response:
    logger.info("index page requested")
    return web.Response(text="Index page.")


async def health(request: web.Request) -> web.Response:
    logger.info("health check requested")
    return web.Response(text="Ok", status=200)
