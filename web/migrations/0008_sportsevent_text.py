# Generated by Django 2.0.2 on 2018-06-24 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20180624_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportsevent',
            name='text',
            field=models.TextField(default=123),
            preserve_default=False,
        ),
    ]
