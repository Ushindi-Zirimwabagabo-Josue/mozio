# Generated by Django 3.2.12 on 2022-02-26 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicearea',
            old_name='polygon',
            new_name='geojson',
        ),
        migrations.AlterField(
            model_name='servicearea',
            name='name',
            field=models.CharField(max_length=256),
        ),
    ]
