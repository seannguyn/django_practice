# Generated by Django 2.0.5 on 2018-08-16 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accomodation', '0006_auto_20180816_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='accomodation',
            name='area',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='accomodation',
            name='bathroom',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='accomodation',
            name='bedroom',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='accomodation',
            name='bedroom_master',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='accomodation',
            name='carpark',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accomodation',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='accomodation',
            name='entertainment',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accomodation',
            name='floors',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='accomodation',
            name='gym',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accomodation',
            name='kitchen',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='accomodation',
            name='laundry',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accomodation',
            name='pool',
            field=models.IntegerField(default=0),
        ),
    ]