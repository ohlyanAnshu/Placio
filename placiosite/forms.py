from django import forms
from .models import *

class postYourReq(forms.ModelForm):

    class Meta:
        model = PostYourReq
        fields = ('name','email','phone_number','city','area','budget', 'roomtype','comment')

class franchise(forms.ModelForm):

    class Meta:
        model = Franchise
        fields = ('name','email','mobile_number','typeofproperty','NumberofBedrooms','ExpectedRent','currentStatus','city','address','comment')

class payrentform(forms.ModelForm):

    class Meta:
        model = PayRent
        fields = ('paymentType','propertyname','tenantId','mobile_number','fullname','amount','email')
