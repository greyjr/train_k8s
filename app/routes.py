import logging

from aiohttp import web
from views import health, index, stop

logger = logging.getLogger(__name__)


def web_app() -> web.Application:
    app = web.Application()
    app.add_routes(
        [
            web.get("/", index),
            web.get("/health", health),
            web.get("/stop", stop),
        ]
    )
    return app


async def start_web_server() -> None:
    app = web_app()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner)
    await site.start()
    logger.info("start web server")
