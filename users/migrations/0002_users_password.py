# Generated by Django 4.1.5 on 2023-03-08 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default='xyz', max_length=13),
        ),
    ]
