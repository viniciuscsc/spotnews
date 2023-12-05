from django.db import models


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
