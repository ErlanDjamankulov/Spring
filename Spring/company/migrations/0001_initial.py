# Generated by Django 5.0.3 on 2024-03-22 13:19

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
                ('id', models.SmallIntegerField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=128)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('timetable', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField(default=0)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
    ]
