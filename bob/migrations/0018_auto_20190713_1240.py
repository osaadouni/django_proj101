# Generated by Django 2.2.3 on 2019-07-13 10:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bob', '0017_bobhandeling_dvom_strafvorderlijkebevoegdheidid'),
    ]

    operations = [
        migrations.AddField(
            model_name='bobhandeling',
            name='dvom_verlengingnr',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='Hoeveelste verlenging betreft het', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Verlenging nr'),
        ),
        migrations.AlterField(
            model_name='bobhandeling',
            name='dvom_heeftverlenging',
            field=models.BooleanField(blank=True, choices=[(True, 'Ja'), (False, 'Nee')], default=False, null=True, verbose_name='Heeft verlenging'),
        ),
        migrations.AlterField(
            model_name='bobhandeling',
            name='dvom_heterdaad',
            field=models.BooleanField(blank=True, choices=[(True, 'Ja'), (False, 'Nee')], default=False, null=True, verbose_name='Heterdaad'),
        ),
        migrations.AlterField(
            model_name='bobhandeling',
            name='dvom_machtiging_aantal',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='Periode van de machtiging  \n                                             (aantal i.c.m.volgend veld)', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Machtiging aantal (periode)'),
        ),
        migrations.AlterField(
            model_name='bobhandeling',
            name='dvom_machtiging_periode',
            field=models.CharField(blank=True, choices=[('DD', 'Dag/Dagen'), ('WW', 'Week/Weken'), ('MM', 'Maand/Maanden')], help_text='Eenheid van de periode van de machtiging ', max_length=2, null=True, verbose_name='Machtiging periode (eenheid)'),
        ),
        migrations.AlterField(
            model_name='bobhandeling',
            name='dvom_machtigingdoorid',
            field=models.CharField(blank=True, help_text='RC die de machtiging afgeeft (id van de gebruiker \n                                             in de applicatie)', max_length=10, null=True, verbose_name='Machtiging door'),
        ),
        migrations.AlterField(
            model_name='bobhandeling',
            name='dvom_machtigingeinddatum',
            field=models.DateField(blank=True, help_text='Einddatum van de machtiging', null=True, verbose_name='Machtiging einddatum'),
        ),
        migrations.AlterField(
            model_name='bobhandeling',
            name='dvom_machtigingop',
            field=models.DateField(blank=True, help_text='Datum waarop de machtiging is afgegeven', null=True, verbose_name='Machtiging op'),
        ),
        migrations.AlterField(
            model_name='bobhandeling',
            name='dvom_machtigingstartdatum',
            field=models.DateField(blank=True, help_text='Startdatum van de machtiging', null=True, verbose_name='Machtiging startdatum / op'),
        ),
        migrations.AlterField(
            model_name='bobhandeling',
            name='dvom_onderzoeksinstantiecontactpersoon',
            field=models.CharField(blank=True, help_text='Contactpersoon bij de opsporingsinstantie', max_length=100, null=True, verbose_name='Contactpersoon onderzoeksinstantie'),
        ),
        migrations.AlterField(
            model_name='bobhandeling',
            name='dvom_onderzoekstype',
            field=models.CharField(blank=True, choices=[('SO', 'Strafrechtelijk Onderzoek'), ('SF', 'Strafrechtelijk Financieel Onderzoek'), ('SE', 'Strafrechtelijk Executie Onderzoek')], help_text='Type onderzoek (wordt afgeleid van de bevoegdheid)', max_length=2, null=True, verbose_name='Onderzoekstype'),
        ),
        migrations.AlterField(
            model_name='bobhandeling',
            name='dvom_oorspronkelijkebobhandelingid',
            field=models.CharField(blank=True, help_text='ID van de 1e BOB handeling waar \n                                                          de verlenging bij hoort', max_length=100, null=True, verbose_name='Oorspronkelijke BOB handeling'),
        ),
        migrations.AlterField(
            model_name='bobhandeling',
            name='dvom_verbalisant',
            field=models.CharField(help_text='Naam van de verbalisant', max_length=100, verbose_name='Naam verbalisant'),
        ),
        migrations.AlterField(
            model_name='bobhandeling',
            name='dvom_verbalisantcontactgegevens',
            field=models.EmailField(help_text='Contactgegevens van de verbalisant', max_length=254, verbose_name='E-mail verbalisant'),
        ),
        migrations.AlterField(
            model_name='bobhandeling',
            name='dvom_voorgaandebobhandelingid',
            field=models.CharField(blank=True, help_text='ID voorgaande BOB handeling (igv verlenging)', max_length=100, null=True, verbose_name='Voorgaande BOB handeling'),
        ),
    ]