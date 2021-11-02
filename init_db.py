from tortoise import Tortoise, run_async

from recipes_book import settings


async def init():
    db_url = f'postgres://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}/{settings.DB_NAME}'
    await Tortoise.init(
        db_url=db_url,
        modules={'models': ['recipes_book.models']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()


if __name__ == '__main__':
    run_async(init())
