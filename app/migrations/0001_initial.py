# Generated by Django 5.0.2 on 2024-02-08 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BMW',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.CharField(max_length=250)),
                ('islike', models.BooleanField(default=True)),
            ],
        ),
    ]
