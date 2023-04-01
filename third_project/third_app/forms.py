from third_app.models import User

from django import forms


# to connect to model use model form
class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
