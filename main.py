from aiohttp import web

from recipes_book.app import create_app


if __name__ == '__main__':
    app = create_app()
    web.run_app(app)
