from django.db import models
from django.contrib.auth.models import User


class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotografia = models.ImageField(upload_to='artigos/', blank=True, null=True)
    link_externo = models.URLField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='artigos')

    class Meta:
        verbose_name_plural = "Artigos"
        ordering = ['-data_criacao']

    def __str__(self):
        return self.titulo

    def total_likes(self):
        return self.likes.count()


class Like(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='likes')
    session_key = models.CharField(max_length=40)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('artigo', 'session_key')

    def __str__(self):
        return f"Like em {self.artigo.titulo}"


class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Comentários"
        ordering = ['-data']

    def __str__(self):
        return f"Comentário de {self.autor.username} em {self.artigo.titulo}"
