from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#Model for Users
class User(AbstractUser):
    nif = models.IntegerField(blank=True, default=1)

#Model for Squares
class Parcela(models.Model):
    sku = models.CharField(max_length=100)
    dono = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    os_choice = (
        ('Cenouras', 'Cenouras'), 
        ('Batatas', 'Batatas'), 
        ('Feijões', 'Feijões'), 
        ('Alho Francês', 'Alho Francês'), 
        ('Couve Portuguesa', 'Couve Portuguesa'),
        ('Bróculos', 'Bróculos'),
        ('Alface', 'Alface'),
        ('Tomate', 'Tomate')
    )
    conteudo = models.CharField(max_length=64, blank=True, null=True, choices=os_choice)
    status = models.CharField(max_length=100)
    relatorio = models.TextField()
    imagem1 = models.ImageField(upload_to = 'reports/', blank=True)
    imagem2 = models.ImageField(upload_to = 'reports/', blank=True)
    imagem3 = models.ImageField(upload_to = 'reports/', blank=True)
    imagem4 = models.ImageField(upload_to = 'reports/', blank=True)
    imagem5 = models.ImageField(upload_to = 'reports/', blank=True)
    imagem6 = models.ImageField(upload_to = 'reports/', blank=True)
    shipping = (
        ('Não-Enviado', 'Nã-Enviado'), 
        ('Enviado', 'Enviado'), 
        ('Recebido', 'Recebido'),  
    )
    envio = models.CharField(max_length=64, blank=True, null=True, choices=shipping)