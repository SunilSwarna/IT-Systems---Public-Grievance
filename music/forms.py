from django.contrib.auth.models import User
from django import forms
from .models import Transport,Profile
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:

        model=User
        fields=['username','email','password']
<<<<<<< HEAD
        labels={'email':'Email-Id',
                'username':'USERNAME',
                }
=======
         labels={'email':'Email-Id',
                'username':'USERNAME',
                }

>>>>>>> 9e1fff4eb7e65cd445d5c9e930d81ae3f4d43249

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
