# Generated by Django 3.0.6 on 2020-05-28 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloader', '0002_auto_20200519_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='status',
            field=models.CharField(choices=[(0, 'Failed'), (1, 'Pending'), (2, 'Done')], default=1, max_length=64),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='url',
            field=models.SlugField(max_length=1024),
        ),
    ]
