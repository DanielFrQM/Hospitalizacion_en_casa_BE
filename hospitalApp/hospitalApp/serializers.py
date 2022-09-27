from dataclasses import fields
from rest_framework import serializers
from .models import Auxiliar

class AuxiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auxiliar
        fields = ('id', 'nombre_aux', 'apel_aux', 'direc_aux')