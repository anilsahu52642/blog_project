from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.forms import widgets
from django.forms.models import ModelFormMetaclass
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from django.utils.translation import gettext, gettext_lazy as _
from .models import blog
from django.contrib.auth.forms import PasswordResetForm

# for signup ..............
class signupform(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'anilform'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'anilform'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']
        widgets={'username':forms.TextInput(attrs={'class':'anilform'}),
        'email':forms.EmailInput(attrs={'class':'anilform'}),
        'first_name':forms.TextInput(attrs={'class':'anilform'}),
        'last_name':forms.TextInput(attrs={'class':'anilform'}),
        }
        help_texts={'username':None,'first_name':None,'last_name':None}


# for signin to account..................
class signinform(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'anilform'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'anilform'}))

# for changeing the password if previous password is known.................
class pchangeform(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True,'class':'anilform'}),
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'anilform'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'anilform'}),
    )

# for creating one blog page..........
class createblogform(forms.ModelForm):
    class Meta:
        model=blog
        fields=['title','content','photo']
        widgets={
            'title':forms.TextInput(attrs={'class':'anilform'}),
            'content':forms.Textarea(attrs={'class':'anilform'}),
            'photo':forms.FileInput(attrs={'class':'anilform'})

        }



# for reseting password.................
class presetform(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email','class':'anilform'})
    )

class newpasswordform(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'anilform'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'anilform'}),
    )