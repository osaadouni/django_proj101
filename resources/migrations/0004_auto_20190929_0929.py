# Generated by Django 2.2.3 on 2019-09-29 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_auto_20190929_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bobaanvraag',
            name='pv_verdenking',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='resources.PvVerdenking'),
        ),
    ]