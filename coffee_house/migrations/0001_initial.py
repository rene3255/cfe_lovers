# Generated by Django 4.1.1 on 2022-10-21 18:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeeHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('city', models.CharField(blank=True, max_length=150, null=True)),
                ('wifi', models.BooleanField(choices=[(True, 'Si'), (False, 'No')], default=True)),
                ('open_area', models.BooleanField(choices=[(True, 'Si'), (False, 'No')], default=False)),
                ('silence_area', models.BooleanField(choices=[(True, 'Si'), (False, 'No')], default=False)),
                ('vegan', models.BooleanField(choices=[(True, 'Si'), (False, 'No')], default=False)),
                ('price_rate', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(1)])),
                ('origen', models.CharField(blank=True, max_length=255, null=True)),
                ('machine', models.CharField(blank=True, max_length=255, null=True)),
                ('grinder', models.CharField(blank=True, max_length=255, null=True)),
                ('barista', models.CharField(blank=True, max_length=255, null=True)),
                ('schedule', models.CharField(blank=True, max_length=255, null=True)),
                ('latitude', models.CharField(blank=True, max_length=255, null=True)),
                ('longitude', models.CharField(blank=True, max_length=255, null=True)),
                ('coffee_image', models.ImageField(blank=True, null=True, upload_to='coffees_images/')),
                ('stars_average', models.DecimalField(decimal_places=1, default=0.5, max_digits=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-updated_at', '-created_at'],
            },
        ),
    ]
