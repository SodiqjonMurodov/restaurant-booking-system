# Generated by Django 5.1.2 on 2024-10-28 06:44

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone1', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message='Enter a valid phone number.', regex='^\\+?\\d{9,13}$')])),
                ('phone2', models.CharField(blank=True, max_length=13, null=True, validators=[django.core.validators.RegexValidator(message='Enter a valid phone number.', regex='^\\+?\\d{9,13}$')])),
                ('address', models.CharField(max_length=255)),
                ('about_us', models.TextField()),
                ('coordinate', models.TextField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('header_image', models.ImageField(blank=True, null=True, upload_to='layout')),
                ('title_image', models.ImageField(blank=True, null=True, upload_to='layout')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='layout')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Cooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='cooks')),
                ('skill', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Cook',
                'verbose_name_plural': 'Cooks',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery')),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Gallery',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='posts')),
                ('media_link1', models.TextField(blank=True, null=True)),
                ('media_link2', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle1', models.CharField(max_length=150)),
                ('subtitle2', models.CharField(blank=True, max_length=150, null=True)),
                ('description1', models.TextField()),
                ('description2', models.TextField(blank=True, null=True)),
                ('description3', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='services')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='testimonials')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonials',
            },
        ),
        migrations.CreateModel(
            name='MediaLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messanger', models.CharField(choices=[('email', 'Email'), ('facebook', 'Facebook'), ('telegram', 'Telegram'), ('instagram', 'Instagram')], default='email', max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media_links', to='restaurant.company')),
            ],
            options={
                'verbose_name': 'Social Network Link',
                'verbose_name_plural': 'Social Network Links',
            },
        ),
    ]
