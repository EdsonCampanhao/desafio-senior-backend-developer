from tortoise.models import Model
from tortoise import fields

class BilheteUnico(Model):
    user = fields.ForeignKeyField("models.User")
    amount = fields.DecimalField(max_digits=10, decimal_places=2)