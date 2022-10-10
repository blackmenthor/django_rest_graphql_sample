from rest_framework import serializers

from animal.serializers import AnimalSerializer
from keeper.models import AnimalKeeper


class AnimalKeeperSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(read_only=True)

    class Meta:
        model = AnimalKeeper
        fields = '__all__'
