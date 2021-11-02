import json

from aiohttp import web
from hashlib import sha256

from recipes_book.models import User


async def register(request):
    try:
        data = await request.json()
    except json.JSONDecodeError:
        raise web.HTTPBadRequest(text='invalid json')

    if 'name' not in data or 'password' not in data:
        raise web.HTTPBadRequest(text='name or password is required')

    name = data.get('name')
    password = data.get('password')

    if not name or not password:
        raise web.HTTPBadRequest(text='name or password is empty')

    user = await User.get_or_none(name=name)
    if user:
        raise web.HTTPBadRequest(text='user already exists')

    hasher = sha256()
    hasher.update(password.encode())
    await User.create(name=name, password_hash=hasher.hexdigest())

    return web.Response(text='user registered successfully')
