from django.contrib import admin
from .models import Dieta

# Register your models here.
@admin.register(Dieta)
class DietaAdmin(admin.ModelAdmin):
    list_display = ['id', 'descricao', 'ingredientes', 'data_inicio', 'dieta_concluida']
    search_fields = ['id', 'descricao', 'ingredientes', 'dieta_concluida', 'data_inicio' 'data_final', 'data_final']
    list_display_links = ['id', ]
    list_filter = ['data_inicio','data_final','dias_semana',]
    list_editable = ['dieta_concluida',]
    list_per_page = 20
    
    pass
    