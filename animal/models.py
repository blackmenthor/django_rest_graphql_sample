import uuid
from django.db import models


# Create your models here.
class Animal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.TextField(null=False)
    image = models.ImageField(null=False, upload_to='uploads/animal/')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Animal: ' + self.name
