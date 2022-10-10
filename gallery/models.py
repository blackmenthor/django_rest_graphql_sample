import uuid
from django.db import models
from animal.models import Animal
from keeper.models import AnimalKeeper


class AnimalGallery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    for_animal = models.ForeignKey(Animal, related_name="gallery_animal",
                                   on_delete=models.CASCADE, null=True, blank=True)
    for_keeper = models.ForeignKey(AnimalKeeper, related_name="gallery_keeper",
                                   on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(null=False, upload_to='uploads/animal_gallery/')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.for_animal:
            return 'Animal Gallery: ' + self.for_animal.name
        return 'Animal Gallery: ' + self.for_keeper.name
