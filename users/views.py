from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from users.forms import RegisterUserCreationForm
from django.core.mail import send_mail
from django.contrib.auth import login
from django.conf import settings


class RegisterView(CreateView):
    form_class = RegisterUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)
