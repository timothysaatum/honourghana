from .models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    select = forms.MultipleChoiceField(choices=Contact.TICK_WHERE_RELEVANT, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Contact
        fields = '__all__'