# Generated by Django 3.0.5 on 2020-09-14 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updateSystem', '0008_contact_us_enquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
