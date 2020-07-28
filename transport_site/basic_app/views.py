from django.shortcuts import render
from . import models
from django.views.generic import (TemplateView,ListView,
                                    DetailView,CreateView,
                                    UpdateView,DeleteView,
                                    )
from basic_app.models import ContactUs, News
from basic_app.forms import ContactForm
from django.core.mail import send_mail

from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from .forms import ContactForm

class HomeView(TemplateView):
    template_name = 'home.html'

class TeamView(TemplateView):
    template_name = 'team.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class PropertyListView(ListView):
    model = models.PropertyInfo

    def get_queryset(self):
        return models.PropertyInfo.objects.order_by('city_name')

class NewsListView(ListView):
    model = models.News

    def get_queryset(self):
        return models.News.objects.order_by('-date')

class NewsDetailView(DetailView):
    model = models.News

def contactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            message = "{0} at {1} has sent you a new message:\n\n{2}".format(sender_name,sender_email, form.cleaned_data['message'])
            send_mail('TRANSPORT PROPERTIES WEBSITE CONTACT', message, sender_email, ['nfeeney21@gmail.com','nfeeney16@yahoo.com'])
            form = ContactForm()
            return render(request, 'contactus_form.html', {'form':form})
    else:
        form = ContactForm()
    return render(request, 'contactus_form.html', {'form':form})
