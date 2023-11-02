# Generated by Django 4.2.7 on 2023-11-02 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studdb',
            fields=[
                ('sid', models.PositiveIntegerField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('passing_year', models.IntegerField(max_length=4)),
                ('finshing_date', models.DateField()),
                ('age', models.IntegerField(max_length=3)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
