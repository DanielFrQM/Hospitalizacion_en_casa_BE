from django.db import models

# Create your models here.
class Auxiliar(models.Model):
    id = models.AutoField(primary_key=True)
    # user = models.ForeignKey(User, related_name='auxiliar',on_delete=models.CASCADE) #en esta linea se puede ver la relacion con la FK one to Many
    nombre_aux = models.CharField('Nombre_aux', max_length = 30)
    apel_aux = models.CharField('Apel_aux', max_length = 30)
    direc_aux = models.CharField('Direc_aux', max_length = 30)