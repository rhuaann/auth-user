from decimal import Decimal

from django import forms

from .models import Stand


class StandForm(forms.ModelForm):

    localizacao = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
        })
    )
    valor = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "money form-control",
        })
    )

    def clean_valor(self):
        valor = self.cleaned_data["valor"]
        return Decimal(valor.replace(",", "."))

    class Meta:
        model = Stand
        fields = (
            "localizacao",
            "valor",
        )