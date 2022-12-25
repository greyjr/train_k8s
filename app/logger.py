import logging.config
from typing import Any, Mapping

_default_config: Mapping[str, Any] = {
    "handlers": ["console"],
    "propagate": False,
}

STATUS_LOGGER = {"level": "INFO", **_default_config}
HTTP_LOGGER = {"level": "WARNING", **_default_config}
MAIN_LOGGER = {"level": "INFO", **_default_config}
LIBS_LOGGER = {"level": "ERROR", **_default_config}


CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "verbose": {
            "format": "%(asctime)s %(levelname)-5.5s [%(name)s]:%(funcName)s#L%(lineno)s %(message)s",  # noqa
            "datefmt": "%Y-%m-%d %H:%M:%S %z",
        },
    },

    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "uvloop": LIBS_LOGGER,
        "asyncio": LIBS_LOGGER,
        "aiohttp": HTTP_LOGGER,
        "aiohttp.access": HTTP_LOGGER,
        "app": MAIN_LOGGER,
    },
    "root": MAIN_LOGGER,
}

logging.config.dictConfig(CONFIG)
