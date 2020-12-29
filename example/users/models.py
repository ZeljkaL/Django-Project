from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.cache import cache
# Create your models here.
alphanumeric = RegexValidator(
    '^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')


class CustomUser(AbstractUser):

    identification = models.CharField(
        max_length=20, blank=True, unique=True, null=True, validators=[alphanumeric])

    def clean_id(self):
        identification = self.cleaned_data.get("identification")

        if CustomUser.objects.filter(identification=identification).exists():
            raise forms.ValidationError("identification already exists")
        return identification
