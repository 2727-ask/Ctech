# Generated by Django 3.0.5 on 2020-09-09 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updateSystem', '0003_auto_20200909_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('Clients_id', models.AutoField(primary_key=True, serialize=False)),
                ('Clients_name', models.CharField(max_length=150)),
                ('Clients_img', models.ImageField(upload_to='updateSystem/images')),
            ],
        ),
    ]
