# Generated by Django 4.1.1 on 2022-10-04 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platerak', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platerak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('izena', models.CharField(max_length=255)),
                ('prezioa', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Platera',
        ),
    ]
