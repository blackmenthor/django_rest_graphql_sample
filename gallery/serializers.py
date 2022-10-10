from rest_framework import serializers

from animal.serializers import AnimalSerializer
from gallery.models import AnimalGallery
from keeper.serializers import AnimalKeeperSerializer


class AnimalGallerySerializer(serializers.ModelSerializer):
    for_animal = AnimalSerializer(read_only=True)
    for_keeper = AnimalKeeperSerializer(read_only=True)

    class Meta:
        model = AnimalGallery
        fields = '__all__'
