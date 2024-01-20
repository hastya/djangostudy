import random

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserForm
from users.models import User


# Create your views here.
class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    # def form_valid(self, form):
    #     new_user = form.save()
    #     send_mail(
    #         subject='Поздравляем с регистрацией',
    #         message=f'Вы зарегистрировались на нашей платформе, добро пожаловать!',
    #         from_email=settings.EMAIL_HOST_USER,
    #         recipient_list=[new_user.email]
    #     )
    #     return super().form_valid(form)
    def form_valid(self, form):
        new_user = form.save(commit=False)
        verification = gen_verification_code_or_password()
        new_user.email_verification = verification
        new_user.is_active = False
        verification_url = f'http://127.0.0.1:8000/users/activate/{verification}'
        send_mail(
            subject='Подтверждение почты',
            message=f'Подтвердите вашу почту. Перейдите по ссылке: {verification_url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        new_user.save()

        return super().form_valid(form)

class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('catalog:index'))


def gen_verification_code_or_password():
    return ''.join([str(random.randint(0, 9)) for i in range(12)])

def email_activated(request):
    return render(request, "users/email_activated.html")

def activate(request, uid):
    user = get_object_or_404(User, email_verification=uid)
    user.is_active = True
    user.save()
    return redirect(reverse('users:email_activated'))

def restore_password(request):
    if request.method == "POST":
        email = request.POST.get('email')
        user = get_object_or_404(User, email=email)
        new_password = gen_verification_code_or_password()
        send_mail(
            subject='Восстановление пароля',
            message=f'Ваш новый пароль: {new_password}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        user.set_password(new_password)
        user.save()
        return redirect(reverse('users:login'))
    return render(request, "users/restore_password.html")
