# Generated by Django 2.2.4 on 2019-08-21 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appis', '0007_auto_20190821_0735'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='language',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='语言'),
        ),
    ]
