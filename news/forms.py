import hashlib

from django import forms
from .models import *
import os


class LinkForm(forms.Form):
    link = forms.CharField(max_length=100)
    #my_link = forms.CharField(max_length=100)

    #link.widget.attrs.update({'class': 'form-control'})

    def save(self):
        salt = os.urandom(32)
        l = self.cleaned_data['link']
        key = hashlib.pbkdf2_hmac('sha256',
                                  l.encode('utf-8'),
                                  salt,
                                  10000,
                                  dklen=1)
        new_link = Links.objects.create(link=l,
                                        my_link=key)
        return new_link

