from django.contrib.auth.forms import UserCreationForm

from apps.accounts.models import User
from apps.accounts.services.location import get_or_create_location_instance


class UserSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'city_name')

    def save(self, commit=True):
        user = super().save()
        user.location = get_or_create_location_instance(self.cleaned_data.get('city_name'))
        user.save()
        return user
