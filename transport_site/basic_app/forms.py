from django import forms
from basic_app.models import ContactUs


class ContactForm(forms.Form):
        name = forms.CharField(max_length=300)
        email = forms.EmailField()
        message = forms.CharField(widget=forms.Textarea)
