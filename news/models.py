from django.db import models
from django.core.exceptions import ValidationError


def validar_titulo(titulo: str):
    palavras = titulo.split()
    if len(palavras) < 2:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")


class Category(models.Model):
    # "name" não deve aceitar informações vazias ou maiores que 200 caracteres
    name = models.CharField(max_length=200, blank=False)

    # __str__ deve retornar a propriedade name da categoria criada
    def __str__(self) -> str:
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=200, blank=False)
    password = models.CharField(max_length=200, blank=False)
    role = models.CharField(max_length=200, blank=False)

    def __str__(self) -> str:
        return self.name


class News(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[validar_titulo],
    )
    content = models.CharField(blank=False)
    author = models.ForeignKey("User")
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(blank=True)
    categories = models.ManyToManyField("Category")
