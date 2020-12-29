from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
from django.core.cache import cache
from django.urls import include, path
# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    change_form_template = 'loginas/change_form.html'
    readonly_fields = ('identification',)

    list_display = ('username', 'is_active', 'email',
                    'identification', 'LogIn_Number')

    def LogIn_Number(self,  user_id):
        if CustomUser.objects.get(username=user_id):
            result = cache.get('count', version=user_id.pk)
            return result

    fieldsets = (
        (None, {'fields': ('username', 'email', 'first_name',)}),
        ('Permissions', {
         'fields': ('is_staff', 'is_active', 'is_superuser',)}),
        ('Identification', {'fields': ('identification', )}),


    )


admin.site.register(CustomUser, CustomUserAdmin)
