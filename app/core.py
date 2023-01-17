import asyncio
import logging

import settings

from models import trigger

logger = logging.getLogger(__name__)


async def core_loop() -> None:
    trigger.on()
    while trigger.is_on():
        await asyncio.sleep(settings.LOOP_DELAY)
        logger.info("main loop tick ...")

    logger.info("app stopped")
    exit()
