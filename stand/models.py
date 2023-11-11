# from django.db import models
# from users.models import User
# from django.contrib.auth import get_user_model

# Create your models here.
# def get_sentinel_user():
#     return get_user_model().objects.get_or_create(email="deleted")[0]

# class Stand (models.Model):
#     created_by = models.ForeignKey(
#         User,
#         verbose_name=("Created by"),
#         on_delete=models.SET(get_sentinel_user),
#         null=True,
#         related_name="created_%(app_label)s_%(class)s_set",
#     )
#     localizacao = models.CharField(
#         verbose_name=("Localização"), max_length=250
#     )
#     valor = models.DecimalField(
#         verbose_name=("Valor"),
#         decimal_places=2,
#         max_digits=6
#     )
    
#     def __str__(self):
#         return f"{self.pk} | {self.localizacao} | {self.valor}"

from core.constants import SMALL_CHAR_FIELD_NAME_LENGTH
from core.models import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _
from stand.validators import validate_stand_localizacao


class Stand(BaseModel):
 
    localizacao = models.CharField(
        verbose_name=_("Localização"),
        max_length=SMALL_CHAR_FIELD_NAME_LENGTH,

    )
    valor = models.DecimalField(
        verbose_name=_("Valor"),
        decimal_places=2,
        max_digits=6
    )

    class Meta:
        verbose_name = _("Stand")
        verbose_name_plural = _("Stands")

    def __str__(self):
        return f"{self.pk} | {self.localizacao} | {self.valor}"