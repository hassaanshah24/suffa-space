# users/forms.py

from django import forms
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

# Single form for editing user profile
class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'user_type', 'department', 'contact_number']
