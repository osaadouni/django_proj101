# Generated by Django 2.2.3 on 2019-07-10 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bob', '0005_auto_20190710_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='bobhandeling',
            name='dvom_heeftverlenging',
            field=models.BooleanField(choices=[(True, 'Ja'), (False, 'Nee')], default=False, verbose_name='Heeft verlenging'),
        ),
    ]