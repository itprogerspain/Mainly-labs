from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from .models import CustomUser

<<<<<<< HEAD
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # what fields to show in user list
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "avatar_preview")

    # so that you can upload an avatar when editing
    fieldsets = UserAdmin.fieldsets + (
        ("Campos adicionales", {"fields": ("avatar",)}),
    )

    # show avatar thumbnail in list
    def avatar_preview(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" style="height:40px; border-radius:50%;" />')
        return "—"
    avatar_preview.short_description = "Avatar"
=======

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "role",
        "is_staff",
        "avatar_preview",
    )


    fieldsets = UserAdmin.fieldsets + (
        ("Campos adicionales", {"fields": ("avatar", "role", "phone_number")}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Campos adicionales", {"fields": ("avatar", "role", "phone_number")}),
    )


    def avatar_preview(self, obj):
        if obj.avatar:
            return mark_safe(
                f'<img src="{obj.avatar.url}" style="height:40px; border-radius:50%;" />'
            )
        return "—"

    avatar_preview.short_description = "Avatar"
>>>>>>> 9d4fe1e0c27239dd31bc552a1f9dabee119d2833
