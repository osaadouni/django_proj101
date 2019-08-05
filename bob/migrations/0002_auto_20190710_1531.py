# Generated by Django 2.2.3 on 2019-07-10 13:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bob', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bobhandeling',
            name='dvom_datumpv',
            field=models.DateField(default=datetime.date(2019, 7, 10), verbose_name='Datum PV'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bobhandeling',
            name='dvom_verbalisant',
            field=models.CharField(default=None, help_text='Naam van de verbalisant', max_length=100, verbose_name='Verbalisant'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bobhandeling',
            name='dvom_verbalisantcontactgegevens',
            field=models.EmailField(default=None, max_length=254, verbose_name='Verbalisant'),
            preserve_default=False,
        ),
    ]