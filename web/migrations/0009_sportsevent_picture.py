# Generated by Django 2.0.2 on 2018-06-24 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_sportsevent_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportsevent',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='static/eventspic/'),
        ),
    ]
