# Generated by Django 3.2.16 on 2022-12-27 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20221227_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reader',
            name='path_to_find',
        ),
        migrations.AlterField(
            model_name='reader',
            name='path_to_manage',
            field=models.URLField(blank=True, default=''),
        ),
    ]
