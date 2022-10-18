from gc import disable
from this import d
from django import forms
from dietas.models import Dieta
from crispy_forms.helper import FormHelper

class dietaform(forms.ModelForm):
    class Meta:
        model = Dieta
        fields = '__all__'


