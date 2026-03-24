from rest_framework import serializers
from .models import Monster

class MonsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monster
        # Include 'slug' so the services can match records correctly
        fields = ['id', 'name', 'slug', 'category', 'description', 'weakness', 'danger_level']
