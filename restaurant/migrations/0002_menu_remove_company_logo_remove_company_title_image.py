# Generated by Django 5.1.2 on 2024-11-02 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='menus')),
                ('file', models.FileField(upload_to='menu-files')),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menu',
            },
        ),
        migrations.RemoveField(
            model_name='company',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='company',
            name='title_image',
        ),
    ]
