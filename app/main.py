from aiohttp import web
from views import health, index

app = web.Application()
app.add_routes(
    [
        web.get("/", index),
        web.get("/health", health)
    ]
)
web.run_app(app)
