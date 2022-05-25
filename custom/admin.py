from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from custom.models import (
	UserCategory, User
)
# Register your models here.


# UserCategory register to admin
class UserCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('cr_date',)


admin.site.register(UserCategory, UserCategoryAdmin)


# User register to admin
class UserAdmin(admin.ModelAdmin):
    list_display = (
    	'first_name', 'last_name', 'email', 'phone_number',
    )
    search_fields = (
    	'first_name', 'last_name', 'email', 'phone_number',
    )
    list_filter = ('date_joined',)


admin.site.register(User, UserAdmin)