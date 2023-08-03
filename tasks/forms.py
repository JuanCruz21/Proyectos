from django import forms

class Signup(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    password = forms.PasswordInput()