# Generated by Django 4.1.1 on 2022-11-18 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dieta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_dieta', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('ingredientes', models.TextField()),
                ('dias_semana', multiselectfield.db.fields.MultiSelectField(choices=[('Seg', 'Segunda-Feira'), ('Ter', 'Terça-Feira'), ('Qua', 'Quarta-Feira'), ('Qui', 'Quinta-Feira'), ('Sex', 'Sexta-feira'), ('Sab', 'Sabado'), ('Dom', 'Domingo')], default='Seg', max_length=27)),
                ('carbo', models.IntegerField()),
                ('calorias', models.IntegerField()),
                ('dieta_concluida', models.BooleanField(default=False)),
                ('data_inicio', models.DateField()),
                ('data_final', models.DateField()),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dieta',
            },
        ),
    ]
