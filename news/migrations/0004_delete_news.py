# Generated by Django 3.2.2 on 2021-06-14 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_links_count'),
    ]

    operations = [
        migrations.DeleteModel(
            name='News',
        ),
    ]
