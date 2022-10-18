from gc import disable
from this import d
from django import forms
from dietas.models import Dieta
from tempus_dominus.widgets import DatePicker
from datetime import datetime

class dietaform(forms.ModelForm):
    data_final = forms.DateField(label="Data da Pesquisa", initial=datetime.today())
    class Meta:
        model = Dieta
        fields = '__all__'
        widgets = {
            'data_ida': DatePicker(),
            'pessoa': forms.HiddenInput,
        }


