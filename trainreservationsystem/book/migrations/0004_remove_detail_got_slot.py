# Generated by Django 3.0.3 on 2020-04-24 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_detail_got_slot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='got_slot',
        ),
    ]