# Generated by Django 3.2.4 on 2021-06-28 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remainderapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1996-03-6'),
            preserve_default=False,
        ),
    ]
