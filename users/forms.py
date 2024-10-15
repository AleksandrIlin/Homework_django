from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser


class RegisterUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False, help_text="Необязательное поле для ввода. Введите ваш номер телефона.")
    username = forms.CharField(max_length=50, required=True)

    class Meta:
        model = CustomUser
        fields = ("email", "username", "avatar", "first_name", "phone_number", "password1", "password2")

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен состоять только из цифр')
        return phone_number
