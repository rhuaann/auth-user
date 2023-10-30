# from django.db import models
# from stand.models import Stand

# class Reserva (models.Model):
#     cnpj= models.CharField(max_length=100)
#     nome_empresa= models.CharField(max_length=100)
#     categoria_empresa= models.CharField(max_length=100)
#     quitado= models.BooleanField()
#     stand=models.ForeignKey(Stand,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return f"{self.pk} | {self.nome_empresa} | {self.cnpj} | {self.quitado}"


from django.db import models
from django.utils.translation import gettext_lazy as _

from core.constants import (MAX_CHAR_FIELD_NAME_LENGTH,
                            MEDIUM_CHAR_FIELD_NAME_LENGTH,
                            SMALL_CHAR_FIELD_NAME_LENGTH)
from core.models import BaseModel
from stand.models import Stand


class Reserva(BaseModel):
    class Categoria(models.TextChoices):
        TEC = "TECNOLOGIA", _("Tecnologia")
        AGRO = "AGRO", _("Agro Negócio")

    cnpj_empresa = models.CharField(
        verbose_name=_("CNPJ Empresa"), max_length=SMALL_CHAR_FIELD_NAME_LENGTH
    )
    nome_empresa = models.CharField(
        verbose_name=_("Nome Empresa"), max_length=MAX_CHAR_FIELD_NAME_LENGTH
    )
    categoria_empresa = models.CharField(
        verbose_name=_("Categoria Empresa"),
        max_length=SMALL_CHAR_FIELD_NAME_LENGTH,
        choices=Categoria.choices,
    )
    quitado = models.BooleanField(_("Quitado"), default=False)
    stand = models.ForeignKey(
        Stand,
        verbose_name=_("Stand"),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("Reserva")
        verbose_name_plural = _("Reservas")

    def __str__(self):
        return f"{self.pk} | {self.nome_empresa} | {self.quitado}"