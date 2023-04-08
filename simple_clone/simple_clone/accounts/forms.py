from dataclasses import field
from typing import Any

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        field = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        # set custom labels as below
        self.fields["username"].label = "Display Name"
        self.fields["email"].label = "Enter Email Address"
