from tortoise.models import Model
from tortoise import fields

class User(Model):
    name = fields.CharField(max_length=255,unique="true")
    email = fields.CharField(max_length=255,unique="true")
    password = fields.BinaryField()