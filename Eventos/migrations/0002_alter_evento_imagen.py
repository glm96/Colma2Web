# Generated by Django 4.2.1 on 2023-07-25 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eventos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='imagen',
            field=models.ImageField(upload_to='eventos'),
        ),
    ]
