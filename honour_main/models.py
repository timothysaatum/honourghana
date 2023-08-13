from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField


#contact model
class Contact(models.Model):
    TICK_WHERE_RELEVANT = [
        ('CHG','Collaborate with Honoour Ghana'),
        ('CCP','Create a Culture of Honour at my Work Place'),
        ('JHC', 'Join an Honour Champions Community'),
        ('PSF', 'Be a Partner or Sponsor of short films'),
        ('PFH', 'Pitch a short film about Honour'),
        ('HSS', 'Honour someone special'),
        ('OEY', 'Other enquiry')
    ]
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = PhoneNumberField()
    select = models.JSONField(max_length=3, choices=TICK_WHERE_RELEVANT)
    your_message = models.TextField()

    def __str__(self):
        return self.name


class New(models.Model):
    CATEGORIES = [
        ('others','others'),
        ('newsletter', 'newsletter')
        ]
    title = models.CharField(max_length=100)
    select_category = models.CharField(max_length=15, default='others', choices=CATEGORIES)
    content = RichTextField()
    feed_url = models.SlugField()

    def __str__(self):
        return self.title