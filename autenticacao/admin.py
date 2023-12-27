from django.contrib import admin
from .models import User
from django.contrib.auth import admin as admin_auth
from .form import UserChangeForm, UserCreationForm


@admin.register(User)
class UsersAdmin(admin_auth.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User