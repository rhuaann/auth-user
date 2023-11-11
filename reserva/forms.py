

# from decimal import Decimal

# from django import forms

# from .models import Reserva

# from stand.models import Stand


# class ReservaForm(forms.ModelForm):

#     cnpj = forms.CharField(
#         widget=forms.TextInput(attrs={
#             "class": "form-control cnpj",
#             # "placeholder": "CNPJ da Empresa",
#         })
#     )
#     nome_empresa = forms.CharField(
#         widget=forms.TextInput(attrs={
#             "class": "form-control",
#             # "placeholder": "Nome da Empresa",
#         })
#     )

#     categoria_empresa = forms.CharField(
#         widget=forms.TextInput(attrs={
#             "class": "form-control",
#             # "placeholder": "Categoria da Empresa",
#         })
#     )

#     quitado = forms.BooleanField(
#         required=False,
#         widget=forms.CheckboxInput(attrs={
#             "class": "form-check-input",
#             "style":"width: 25px; height: 25px",
#             "type":"radio",
#         })
#     )
#     stand = forms.ModelChoiceField(
#         queryset=Stand.objects.all(),
#         label="Stand",
#         required=True,
#         widget=forms.Select(attrs={
#             "class": "form-select",
#         })
#     )

#     def clean_valor(self):
#         valor = self.cleaned_data["valor"]
#         return Decimal(valor.replace(",", "."))

#     class Meta:
#         model = Reserva
#         fields = (
#             "cnpj",
#             "nome_empresa",
#             "categoria_empresa",
#             "quitado",
#             "stand",
#         )


from django import forms
from decimal import Decimal
from reserva.models import Reserva
from stand.models import Stand


class ReservaForm(forms.ModelForm):

    cnpj_empresa = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control cnpj",
            "placeholder": "CNPJ da empresa",
        })
    )
    nome_empresa = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Nome da empresa",
        })
    )
    categoria_empresa = forms.ChoiceField(
        choices=Reserva.Categoria.choices,
        label="Cetagoria",
        widget=forms.Select(attrs={
            "class": "form-control",
            "placeholder": "Categoria da Empresa",
        })
    )
    stand = forms.ModelChoiceField(
        queryset=Stand.objects.all(),
        label="Stand",
        required=True,
        widget=forms.Select(attrs={
            "class": "form-select",
        })
    )

    def clean_valor(self):
        valor = self.cleaned_data["valor"]
        return Decimal(valor.replace(",", "."))

    class Meta:
        model = Reserva
        fields = (
            "cnpj_empresa",
            "nome_empresa",
            "categoria_empresa",
            "quitado",
            "stand",
        )