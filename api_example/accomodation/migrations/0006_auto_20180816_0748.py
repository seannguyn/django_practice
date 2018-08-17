# Generated by Django 2.0.5 on 2018-08-16 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accomodation', '0005_auto_20180816_0708'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomStudio',
            fields=[
                ('accommodation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accomodation.Accomodation')),
                ('area', models.IntegerField(default=1)),
                ('bedroom', models.IntegerField(default=1)),
                ('kitchen', models.IntegerField(default=1)),
                ('bathroom', models.IntegerField(default=1)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='houseapartmentvilla',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]