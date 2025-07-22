# forms.py
from django import forms
from .models import Data, Otpp

class DataForm(forms.ModelForm):
    confirm_password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        label="Confirm Password"
    )

    class Meta:
        model = Data
        fields = '__all__'

        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }


class OtppForm(forms.ModelForm):
    class Meta:
        model = Otpp
        fields = ['otp']
