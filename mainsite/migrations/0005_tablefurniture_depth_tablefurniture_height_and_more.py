# Generated by Django 5.0.4 on 2024-04-19 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_alter_material_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablefurniture',
            name='Depth',
            field=models.FloatField(default=0, verbose_name='Глубина'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tablefurniture',
            name='Height',
            field=models.FloatField(default=0, verbose_name='Высота'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tablefurniture',
            name='Width',
            field=models.FloatField(default=0, verbose_name='Ширина'),
            preserve_default=False,
        ),
    ]
