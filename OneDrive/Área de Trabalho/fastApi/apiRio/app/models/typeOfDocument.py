from tortoise.models import Model
from tortoise import fields

class typeOfDocuments(Model):
    name = fields.CharField(max_length=255)
