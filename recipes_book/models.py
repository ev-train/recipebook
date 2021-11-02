from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=512)
    status = fields.BooleanField(default=True)
    password_hash = fields.CharField(max_length=512)

    def __str__(self):
        return self.name


class Recipe(Model):
    author = fields.ForeignKeyField('models.User', related_name='recipes')
    created = fields.DatetimeField(auto_now_add=True)
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField()
    image_url = fields.CharField(max_length=1024)
    recipe_type = fields.CharField(max_length=50)
    status = fields.BooleanField()

    def __str__(self):
        return self.name