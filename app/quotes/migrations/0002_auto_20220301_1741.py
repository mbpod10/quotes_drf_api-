# Generated by Django 3.1.1 on 2022-03-01 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Quotes',
            new_name='Quote',
        ),
    ]