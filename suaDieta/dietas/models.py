from django.db import models
import datetime 

# Create your models here.
class Dieta(models.Model):
    igredientes = models.TextField()
    data_comeco = models.DateTimeField(datetime.datetime.now())
    dieta_publica = models.BooleanField(default=False)
    
    def __str__(self):
        return self.igredientes