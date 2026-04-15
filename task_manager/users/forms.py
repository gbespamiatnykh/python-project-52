from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    UserCreationForm,
)
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


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop("password", None)
