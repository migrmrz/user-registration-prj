from django.forms import ModelForm
from user_registration_app.models import User


class UserRegistrationForm(ModelForm):
    class Meta():
        model = User
        fields = "__all__"
