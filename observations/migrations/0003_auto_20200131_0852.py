# Generated by Django 3.0.2 on 2020-01-31 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0002_auto_20200130_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='comments',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
