from django.utils import timezone

from django.db import models

# Create your models here.
LISTA_CATEGORIAS = (
    ('Ação', 'Ação'),
    ('Aventura', 'Aventura'),
    ('Comédia', 'Comédia'),
    ('Drama', 'Drama'),
)

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=20, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(timezone.now)

