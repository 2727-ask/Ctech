# Generated by Django 3.0.5 on 2020-09-14 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updateSystem', '0007_contact_us_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_us',
            name='enquiry',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
