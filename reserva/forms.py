# from django.forms import ModelForm
# from django import forms
# from .models import Reserva


# class ReservaForm(ModelForm):

#     class Meta:
#         model = Reserva
#         fields = '__all__'
#         widgets = {
#             'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
#             'nome_empresa': forms.TextInput(attrs={'class': 'form-control'}),
#             'categoria_empresa ': forms.TextInput(attrs={'class': 'form-control'}),
#             'quitado ': forms.TextInput(attrs={'class': 'form-control'}),
#             'stand ': forms.Select(attrs={'class': 'form-control'}),
#         }

from decimal import Decimal

from django import forms

from .models import Reserva

from stand.models import Stand


class ReservaForm(forms.ModelForm):

    cnpj = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "CNPJ da Empresa",
        })
    )
    nome_empresa = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Nome da Empresa",
        })
    )

    categoria_empresa = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Categoria da Empresa",
        })
    )

    quitado = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            "class": "form-check",
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

    class Meta:
        model = Reserva
        fields = (
            "cnpj",
            "nome_empresa",
            "categoria_empresa",
            "quitado",
            "stand",
        )