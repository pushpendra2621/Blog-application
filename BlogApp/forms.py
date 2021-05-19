from django import forms
from BlogApp.models import Contact    


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ("name", 'email', 'msg')
