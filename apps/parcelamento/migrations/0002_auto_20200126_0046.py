# Generated by Django 2.2 on 2020-01-26 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parcelamento', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parcelamento',
            old_name='data_final',
            new_name='data',
        ),
    ]