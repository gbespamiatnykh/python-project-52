from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
)
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _

from task_manager.users.models import User


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username"]
        labels = {
            "username": _("Username"),
            "first_name": _("First name"),
            "last_name": _("Last name"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": _("Username")}
        )
        self.fields["first_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": _("First name")}
        )
        self.fields["last_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": _("Last name")}
        )
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": _("Password")}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": _("Password confirmation")}
        )
        self.fields["password1"].help_text = _(
            "Passwords must have at least 3 characters"
        )


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username"]
        labels = {
            "username": _("Username"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": _("Username")}
        )
        self.fields["password"].widget.attrs.update(
            {"class": "form-control", "placeholder": _("Password")}
        )


class UserUpdateForm(forms.ModelForm):
    password1 = forms.CharField(
        required=False, widget=forms.PasswordInput, label=_("Password")
    )
    password2 = forms.CharField(
        required=False,
        widget=forms.PasswordInput,
        label=_("Password confirmation"),
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username"]

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if (password1 or password2) and password1 != password2:
            self.add_error(
                "password2", _("The two password fields didn’t match.")
            )
        try:
            validate_password(password1, self.instance)
        except forms.ValidationError as error:
            self.add_error("password1", error)
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password1")
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user
