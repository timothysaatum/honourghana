# Generated by Django 4.0.4 on 2022-06-01 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('honour_main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='select',
            field=models.CharField(choices=[('Collaborate with Honoour Ghana', 'Collaborate with Honoour Ghana'), ('Create a Culture of Honour at my Work Place', 'Create a Culture of Honour at my Work Place'), ('Join an Honour Champions Community', 'Join an Honour Champions Community'), ('Be a Partner or Sponsor of short films', 'Be a Partner or Sponsor of short films'), ('Pitch a short film about Honour', 'Pitch a short film about Honour'), ('Honour someone special', 'Honour someone special'), ('Other enquiry', 'Other enquiry')], max_length=50),
        ),
    ]
