# Generated by Django 5.0.4 on 2024-04-19 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_alter_material_options_alter_tablefurniture_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='Name',
            field=models.CharField(max_length=50, verbose_name='Название материала'),
        ),
    ]
