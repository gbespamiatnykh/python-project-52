from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from task_manager.users.forms import (
    UserCreatForm,
    UserLoginForm,
    UserUpdateForm,
)

User = get_user_model()


class UsersListView(ListView):
    model = User
    template_name = "users/list.html"
    context_object_name = "users"


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserCreatForm
    template_name = "users/create.html"
    success_url = reverse_lazy("login")
    success_message = _("User created successfully")


class UserLoginView(SuccessMessageMixin, LoginView):
    authentication_form = UserLoginForm
    template_name = "users/login.html"
    success_message = _("Logged in successfully")


class UserLogoutView(LogoutView):
    success_message = _("Logged out successfully")


class UserUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView
):
    model = User
    form_class = UserUpdateForm
    template_name = "users/update.html"
    success_url = reverse_lazy("user_list")
    success_message = _("User updated successfully")

    def test_func(self):
        return self.request.user == self.get_object()

    def handle_no_permission(self):
        messages.error(self.request, _("You do not have permission to change"))
        return redirect("user_list")


class UserDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView
):
    model = User
    template_name = "users/delete.html"
    success_url = reverse_lazy("user_list")
    success_message = _("User deleted successfully")

    def test_func(self):
        return self.request.user == self.get_object()

    def handle_no_permission(self):
        messages.error(self.request, _("You do not have permission to change"))
        return redirect("user_list")
