import asyncio
import logging

import settings

logger = logging.getLogger(__name__)


async def core_loop():
    while True:
        await asyncio.sleep(settings.LOOP_DELAY)
        logger.info("main loop tick ...")
