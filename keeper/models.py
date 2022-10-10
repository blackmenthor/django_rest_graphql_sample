import uuid
from django.db import models
from animal.models import Animal


class AnimalKeeper(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.TextField(null=False)
    origin_country = models.TextField(null=False)
    animal = models.ForeignKey(Animal, related_name="animal_keeper",
                               on_delete=models.CASCADE)
    image = models.ImageField(null=False, upload_to='uploads/animal_keeper/')
    birth_date = models.DateTimeField(null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Animal Keeper: ' + self.name
