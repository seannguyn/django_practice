# Generated by Django 2.0.5 on 2018-08-16 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accomodation', '0004_houseapartmentvilla'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='houseapartmentvilla',
            name='id',
        ),
        migrations.AlterField(
            model_name='houseapartmentvilla',
            name='accommodation',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accomodation.Accomodation'),
        ),
    ]
