from django.shortcuts import render
from rest_framework import viewsets
from .models import Auxiliar
from .serializers import AuxiliarSerializer

# Create your views here.
class AuxiliarView(viewsets.ModelViewSet):
    queryset = Auxiliar.objects.all()
    serializer_class = AuxiliarSerializer