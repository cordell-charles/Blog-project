# Generated by Django 2.2 on 2020-07-22 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200722_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
