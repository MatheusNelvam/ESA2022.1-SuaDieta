from django.db import models
import datetime 
from multiselectfield import MultiSelectField

# Create your models here.
class Dieta(models.Model):
    dias_semana = (
        ("Seg", "Segunda-Feira"),
        ("Ter", "Terça-Feira"),
        ("Qua", "Quarta-Feira"),
        ("Qui", "Quinta-Feira"),
        ("Sex", "Sexta-feira"),
        ("Sab", "Sabado"),
        ("Dom", "Domingo"),
    )
    descricao = models.TextField()
    ingredientes = models.TextField()
    dieta_concluida = models.BooleanField(default=False)
    data_inicio = models.DateTimeField(datetime.datetime.now())
    data_final = models.DateTimeField()
    dias_semana = MultiSelectField(max_length=3, choices=dias_semana, blank=False, null=False, default="Seg" )


    def __str__(self):
        return self.ingredientes

    class Meta:
        verbose_name = "Dieta"