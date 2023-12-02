from playground import CustomUser

from django.contrib.auth.forms import UserChangeForm, UserCreationForm

#django form


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm)   :
        model = CustomUser
        fields = ["username", "email", "year", "password1", "password2"]


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields