from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from.models import CustomUser

#registering the new user model with the admin site, so its visible

class CustomUserAdmin(UserAdmin):
    fieldsets=(
         (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('licence', 'Key', 'is_commision')
        }),

    )
    pass

admin.site.register(CustomUser,CustomUserAdmin)



# Register your models here.
