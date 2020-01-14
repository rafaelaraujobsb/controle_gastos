# Generated by Django 2.2 on 2020-01-14 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0002_auto_20200113_2145'),
        ('cartao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartao',
            name='conta_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='conta.Conta'),
            preserve_default=False,
        ),
    ]
