from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Monster
from .serializers import MonsterSerializer

class MonsterViewSet(viewsets.ModelViewSet):
    queryset = Monster.objects.all()
    serializer_class = MonsterSerializer
    lookup_field = 'slug'
