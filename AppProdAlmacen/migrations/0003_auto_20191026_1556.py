# Generated by Django 2.2.6 on 2019-10-26 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppProdAlmacen', '0002_auto_20191025_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='tipo_contrato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProdAlmacen.Contrato'),
        ),
    ]