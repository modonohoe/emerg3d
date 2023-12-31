from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_moderator', 'is_staff',
                    'is_active', 'slug')
    list_filter = ('is_moderator', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),

        ('Personal info', {
         'fields': ('first_name', 'last_name', 'email', 'slug')}),
        ('Permissions', {'fields': ('is_moderator', 'is_staff', 'is_active', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_moderator', 'is_staff', 'is_active', 'slug')}
         ),
    )

    search_fields = ('username', 'email', 'slug')
    ordering = ('username',)


admin.site.register(CustomUser, CustomUserAdmin)
