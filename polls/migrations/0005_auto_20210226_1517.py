# Generated by Django 3.1.7 on 2021-02-26 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20210225_0958'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='years',
            new_name='votes',
        ),
    ]
