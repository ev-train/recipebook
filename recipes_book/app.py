from aiohttp import web
from tortoise.contrib.aiohttp import register_tortoise

from recipes_book import settings
from recipes_book.routes import setup_routes


def create_app():
    app = web.Application()
    setup_routes(app)
    db_url = f'postgres://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}/{settings.DB_NAME}'
    register_tortoise(app, db_url=db_url, modules={'models': ['recipes_book.models']})
    return app
