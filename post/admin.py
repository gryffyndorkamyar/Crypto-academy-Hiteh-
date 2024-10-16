from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Product, Costumer, Order, Comment, Like, Profile, UserProfile, CostumeUser


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'quantity', 'price']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'username']
    search_fields = ['first_name', 'last_name', 'username']


class CostumeUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'password1', 'password2'),
        }),
    )
    list_display = ['email', 'username', 'first_name', 'is_staff']
    list_filter = ['email', 'username', 'first_name']
    search_fields = ['email', 'username', 'first_name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Costumer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(UserProfile)
admin.site.register(CostumeUser, CostumeUserAdmin)
