# Generated by Django 4.2.5 on 2023-11-02 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postbb',
            options={'ordering': ('-pub_date',)},
        ),
    ]
