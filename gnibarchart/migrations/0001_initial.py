# Generated by Django 4.0 on 2022-01-03 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndicatorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(default='YR----', max_length=6)),
                ('indicator', models.CharField(choices=[('SP.DYN.TFRT.IN', 'Total Fertility Rate')], max_length=50)),
            ],
        ),
    ]