# Generated by Django 3.2.9 on 2021-12-04 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSocial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='perfil_vacio.png', upload_to=''),
        ),
    ]
