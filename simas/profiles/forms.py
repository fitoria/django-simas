from django.forms import ModelForm
from django impot forms
from models import UserProfile, AREA_CHOICES

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']

class UserForm(modelForm):
    class Metal:
        model = User
        exclude = ['password', 'is_staff', 'is_active',
                   'is_superuser', 'last_login', 'date_joined',
                   'username', 'groups', 'user_permissions']

