from django.forms import ModelForm
from app.models import Carros
from app.models import Lanches
from app.models import *
from django import forms
# Create the form class.
class CarrosForm(ModelForm):
    class Meta:
        model = Carros
        fields = ['modelo', 'marca', 'ano']


class LanchesForm(ModelForm):
    class Meta:
        model = Lanches
        fields = ['nome', 'tipo', 'data_pedido', 'horario', 'qtd', 'total', 'status_pgto', 'tipo_pgto', 'data_pgto']




