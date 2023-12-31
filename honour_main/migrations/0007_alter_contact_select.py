# Generated by Django 4.0.4 on 2022-06-01 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('honour_main', '0006_rename_news_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='select',
            field=models.CharField(choices=[('CHG', 'Collaborate with Honoour Ghana'), ('CCP', 'Create a Culture of Honour at my Work Place'), ('JHC', 'Join an Honour Champions Community'), ('PSF', 'Be a Partner or Sponsor of short films'), ('PFH', 'Pitch a short film about Honour'), ('HSS', 'Honour someone special'), ('OEY', 'Other enquiry')], default='CHG', max_length=3),
        ),
    ]
