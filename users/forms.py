from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Row, Layout, Field

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=255)
    first_name = forms.CharField(required=True, max_length=63)
    last_name = forms.CharField(required=True, max_length=63)
    date_of_birth = forms.DateField(required=True, widget=forms.SelectDateWidget())

    class Meta():
        model = get_user_model()
        fields = ["email", "first_name", "last_name", "date_of_birth", "password1", "password2"]

    helper = FormHelper()
    helper.layout = Layout(
        Row(
            Field('email')
        ),
        Row(
            Field('first_name'), Field('last_name')
        ),
        Row(
            Field('date_of_birth')
        ),
        Row(
            Field('password1'),
        ),
        Row(
            Field('password2')
        )
    )
