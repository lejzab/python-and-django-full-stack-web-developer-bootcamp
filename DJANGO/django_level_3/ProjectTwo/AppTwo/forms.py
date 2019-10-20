from django import forms
from . import models

class NewUserForm(forms.ModelForm):

    class Meta:
        model = models.User
        fields = '__all__'
