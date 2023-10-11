from django.db import models

# Create your models here.

class Stand (models.Model):
    localizacao = models.CharField(
        verbose_name=("Localização"), max_length=250
    )
    valor = models.DecimalField(
        verbose_name=("Valor"),
        decimal_places=2,
        max_digits=6
    )
    
    def __str__(self):
        return f"{self.pk} | {self.localizacao} | {self.valor}"
