# Generated by Django 5.1.2 on 2024-10-30 10:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message='Enter a valid phone number.', regex='^\\+?\\d{9,13}$')])),
                ('email', models.EmailField(max_length=254)),
                ('day', models.DateField()),
                ('time', models.TimeField()),
                ('guests', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('confirmation_token', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Bookings',
            },
        ),
    ]
