from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.forms import SetPasswordForm
from django.core.validators import MinLengthValidator



class SingUpForm(UserCreationForm):
    '''User Sign Up form'''
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'required'}),help_text="enter first name")
    last_name = forms.CharField(required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={'id': 'required'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', ]
        placeholders = {
            'username': 'Enter your username',
            'email': 'Enter your email address',
            'first_name': 'Enter your first name',
            'last_name': 'Enter your last name',
            'password1': 'Enter a password',
            'password2': 'Confirm your password',
        }
    def __init__(self, *args, **kwargs):
        super(SingUpForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field in self.Meta.placeholders:
                self.fields[field].widget.attrs['placeholder'] = self.Meta.placeholders[field]

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email



class EmailForOTPForm(forms.Form):
    '''Take Email for send otp'''
    email = forms.CharField(widget=forms.EmailInput(attrs={'id': 'required'}))

class OTPForm(forms.Form):
    '''Take OTP for validation'''
    otp = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))


class NewPasswordForm(forms.Form):
    '''Reset password and set new password form'''
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'id': 'required'}),
        validators=[MinLengthValidator(limit_value=8, message="Password must be at least 8 characters.")]
    )
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'required'}))

    def clean(self):
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        # print(new_password, confirm_password)
        if new_password and confirm_password and new_password != confirm_password: # check new password and confirm password same
            raise forms.ValidationError("new password and confirm password are not same!")