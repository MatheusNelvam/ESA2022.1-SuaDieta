from gc import disable
from this import d
from django import forms
from dietas.models import Dieta

class dietaform(forms.ModelForm):
    class Meta:
        model = Dieta
        fields = '__all__'
        

