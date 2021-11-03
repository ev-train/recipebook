import json

from aiohttp import web
from aiohttp.web_response import json_response
from aiohttp_security import authorized_userid

from recipes_book.models import Recipe, User

async def profile(request):
    user_id = request.match_info['user_id']
    user = await User.get_or_none(id=user_id)
    data = {
        "id": user.id,
        "name": user.name,
        "status": user.status
    }
    return web.json_response(data)

async def new_recipe(request):
    user_id = await authorized_userid(request)
    if user_id is None:
        raise web.HTTPBadRequest(text='login or register')
    try:
        data = await request.json()
    except json.JSONDecodeError:
        raise web.HTTPBadRequest(text='invalid json')

    if 'name' not in data or 'description' not in data or 'image_url' not in data or 'recipe_type' not in data:
        raise web.HTTPBadRequest(text='all fields are required')

    name = data.get('name')
    description = data.get('description')
    image_url = data.get('image_url')
    recipe_type = data.get('recipe_type')

    if not name or not description or not image_url or not recipe_type:
        raise web.HTTPBadRequest(text='field is empty')

    await Recipe.create(id=user_id, name=name, description=description, image_url=image_url, recipe_type=recipe_type, status=True)

    return web.Response(text='recipe added')