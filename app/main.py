import asyncio
from contextlib import suppress

import logger  # noqa
from core import core_loop
from routes import start_web_server


async def main() -> None:
    await start_web_server()
    await core_loop()


if __name__ == "__main__":
    with suppress(KeyboardInterrupt):
        asyncio.run(main())
