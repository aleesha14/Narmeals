# Generated by Django 3.1.7 on 2021-04-27 17:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('narmeal', '0003_auto_20210427_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monday',
            name='dinner',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='monday',
            name='lunch',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
