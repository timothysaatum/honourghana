# Generated by Django 4.0.4 on 2022-06-01 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('honour_main', '0010_new_select_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='feed_url',
            field=models.SlugField(default='today-is'),
            preserve_default=False,
        ),
    ]