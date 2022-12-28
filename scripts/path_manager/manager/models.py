from django.db import models
from django.contrib.auth.models import User
import glob

paths = glob.glob("C:/Users/willi/Desktop/PDFS-TESTES/*")
paths2 = glob.glob("C:/Users/willi/Desktop/PDFS-ORG/*")
count = 0

# creating a class time stamp
class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'criado em', auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(
        'modificado em', auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Reader(models.Model):
   
    user_exe = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Usuarios',
        verbose_name='Usuario')
    date = models.DateTimeField('Data inicio', auto_now=True)
    excel_file = models.FileField('Excel Para Leitura de Dados', upload_to='', blank=True, default='')
    path_to_manage = models.CharField("Caminho para Pasta Destino", max_length=150, blank=True, default='')
    path_files = models.CharField("Caminho de Pasta Origem", max_length=150, blank=True, default='')
    status = models.CharField(max_length=15 ,default='Criado')

    # def __str__(self) -> str:
    #     return self.user_exe