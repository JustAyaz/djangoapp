import hashlib

from django import forms
from .models import *
import os


class LinkForm(forms.Form):
    link = forms.CharField(max_length=100)

    def save(self):
        salt = os.urandom(32)
        l = self.cleaned_data['link']
        key = hashlib.pbkdf2_hmac('sha256',
                                  l.encode('ASCII'),
                                  salt,
                                  10000,
                                  dklen=1)
        k = hashlib.sha1(key).hexdigest()[:5]
        new_link = Links.objects.create(link=l,
                                        my_link=k)
        return new_link

