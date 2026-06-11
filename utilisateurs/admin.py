from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from utilisateurs.models import CustomUser 



@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('informations supplémentaires',{
            'fields':('role','telephone','photo')
        }),
    )
