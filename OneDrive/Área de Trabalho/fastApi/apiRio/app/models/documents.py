from tortoise.models import Model
from tortoise import fields

class Documents(Model):
    
    user = fields.ForeignKeyField("models.User")
    typeOfDocument = fields.ForeignKeyField("models.typeOfDocuments")
    issuingBody = fields.CharField(max_length=255)
    dateOfIssue = fields.DateField()
    registrationNumber = fields.IntField()
    
