from django import forms
from .models import *

class postYourReq(forms.ModelForm):

    class Meta:
        model = PostYourReq
        fields = ('name','email','phone_number','city','area','budget', 'roomtype','comment')
