# Generated by Django 2.0.5 on 2018-08-16 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accomodation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accomodation',
            name='Accomodation_Type',
            field=models.CharField(choices=[('Room', 'Room'), ('Studio', 'Studio'), ('Apartment', 'Apartment'), ('House', 'House'), ('Villa', 'Villa')], max_length=10),
        ),
    ]
