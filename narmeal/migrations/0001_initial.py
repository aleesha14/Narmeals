# Generated by Django 3.1.7 on 2021-04-27 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_name', models.CharField(blank=True, max_length=200)),
                ('meal_notes', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Monday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lunch', models.CharField(max_length=200)),
                ('dinner', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tuesday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lunch', models.CharField(max_length=200)),
                ('dinner', models.CharField(max_length=200)),
            ],
        ),
    ]
