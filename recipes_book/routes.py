from recipes_book.views.users import register


def setup_routes(app):
    app.router.add_post('/users/register', register)
