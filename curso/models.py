from django.db import models
from django.utils.html import mark_safe

# Create your models here.


class Curso_info(models.Model):
    titulo = models.CharField(max_length=25)
    descricao = models.TextField()
    data_criacao = models.DateTimeField()
    imagem = models.ImageField(upload_to='imagens')
    
    def _str_(self):
        return self.categoria

class Curso_Ali(models.Model):
    titulo = models.CharField(max_length=25)
    descricao = models.TextField()
    data_criacao = models.DateTimeField()
    imagem = models.ImageField(upload_to='imagens')
    
    def _str_(self):
        return self.categoria

class Curso_Api(models.Model):
    titulo = models.CharField(max_length=25)
    descricao = models.TextField()
    data_criacao = models.DateTimeField()
    imagem = models.ImageField(upload_to='imagens')
    
    def _str_(self):
        return self.categoria