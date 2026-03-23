from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Monster
from .serializers import MonsterSerializer

class MonsterViewSet(viewsets.ModelViewSet):
    queryset = Monster.objects.all()
    serializer_class = MonsterSerializer
    # This single class handles GET (list), POST (create), GET (detail), etc.
