# Generated by Django 3.0.5 on 2020-09-09 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('product_image', models.ImageField(upload_to='updateSystem/images')),
            ],
        ),
    ]
