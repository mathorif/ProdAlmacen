# Generated by Django 2.2.6 on 2019-10-25 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppProdAlmacen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empleados', to='AppProdAlmacen.Area'),
        ),
    ]
