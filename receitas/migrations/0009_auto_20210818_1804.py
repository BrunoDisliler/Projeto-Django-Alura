# Generated by Django 3.2.6 on 2021-08-18 21:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('receitas', '0008_alter_receita_data_receita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 18, 18, 4, 57, 901915)),
        ),
        migrations.AlterField(
            model_name='receita',
            name='ingredientes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='receita',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
