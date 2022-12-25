import logging

from aiohttp import web
from views import health, index

logger = logging.getLogger(__name__)


def web_app() -> web.Application:
    app = web.Application()
    app.add_routes(
        [
            web.get("/", index),
            web.get("/health", health)
        ]
    )
    return app


async def start_web_server() -> None:
    app = web_app()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()
    logger.info("start web server")
