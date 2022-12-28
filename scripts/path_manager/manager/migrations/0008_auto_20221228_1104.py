# Generated by Django 3.2.16 on 2022-12-28 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_reader_path_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='reader',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reader',
            name='excel_file',
            field=models.FileField(blank=True, default='', upload_to='', verbose_name='Excel Para Leitura de Dados'),
        ),
        migrations.AlterField(
            model_name='reader',
            name='path_files',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Caminho de Pasta Origem'),
        ),
        migrations.AlterField(
            model_name='reader',
            name='path_to_manage',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Caminho para Pasta Destino'),
        ),
    ]
