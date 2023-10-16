from django.contrib import admin

# Register your models here.
# Imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from users.models import UserProfile

# START OF FILE: 'admin.py'

# Custom UserProfile Model Called: UserProfile(default: see models.py)
class UserProfileInLine(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "user"

# Class Inherits the BaseUserAdmin, which is UserAdmin within Django Framework
class UserAdmin(BaseUserAdmin):
    inlines = [UserProfileInLine]

# Unregister the default User Model from Admin Dashboard
admin.site.unregister(User)
# Register User and the new UserAdmin* class
admin.site.register(User, UserAdmin)

'''
Made with ❤️
------------
BRANDEN VAN STADEN -
    All rights reserved | September 2023
-------------------------------------
'''
