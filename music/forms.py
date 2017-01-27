from django.contrib.auth.models import User
from django import forms
from .models import Transport,Profile
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:

        model=User
        fields=['username','email','password']
        labels={'email':'Email-Id',
                'username':'USERNAME',
                }

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput)

class UserForm1(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class TransportForm(forms.ModelForm):
  class Meta:

      model=Transport
      fields=['title','logo']