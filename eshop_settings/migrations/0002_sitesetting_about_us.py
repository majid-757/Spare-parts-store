# Generated by Django 3.1.5 on 2021-02-28 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='about_us',
            field=models.TextField(blank=True, null=True, verbose_name='درباره ی ما'),
        ),
    ]
