# Generated by Django 2.1.2 on 2018-12-15 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quests', '0004_auto_20181019_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelvisual',
            name='mtl',
            field=models.URLField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
