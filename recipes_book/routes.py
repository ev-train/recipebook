from recipes_book.views.users import register, login
from recipes_book.views.views import profile, new_recipe


def setup_routes(app):
    app.router.add_post('/register', register)
    app.router.add_post('/login', login)
    app.router.add_route('GET', '/profile/{user_id}', profile, name='profile')
    app.router.add_post('/new_recipe', new_recipe)

