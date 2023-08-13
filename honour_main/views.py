from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .models import Contact, New
from .forms import ContactForm


# Create your views here.
def home(request):
	return render(request, 'honour_main/index.html')


def about(request):
    return render(request, 'honour_main/about.html')

class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'honour_main/contact.html'
    success_url = '/contact/'

def learning_journey(request):
    return render(request, 'honour_main/learning_journey.html')

def leadership(request):
    return render(request, 'honour_main/leadership.html')


class NewsListView(ListView):
    model = New
    template_name = 'honour_main/news.html'


def news(request):
    return render(request, 'honour_main/news.html')

def initiatives(request):
    return render(request, 'honour_main/initiatives.html')

def donate(request):
    return render(request, 'honour_main/donate.html')

def films(request):
    return render(request, 'honour_main/films.html')