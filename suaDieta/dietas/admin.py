from django.contrib import admin
from .models import Dieta

# Register your models here.
@admin.register(Dieta)
class DietaAdmin(admin.ModelAdmin):
    list_display = ('igredientes', 'data_comeco', 'dieta_publica')
    search_fields = ('igredientes',)
    list_filter = ('data_comeco',)
    list_editable = ['dieta_publica',]
    
    list_per_page = 5
    
    pass
    