from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUSerAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import MyUser
from django.contrib.auth.models import Group

class UserAdmin(BaseUSerAdmin):
    form =UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'phone_number', 'is_admin')
    list_filter = ('is_admin',)

    # for form
    fieldsets = (
        (None, {'fields': ('email','phone_number','full_name','password')}),    # will not make blue block
        ('Permissions', {'fields': ('is_active','is_admin','last_login')}),     # will make a blue block with name Permissions
    )

    # for add_form
    add_fieldsets = (           # which fields will shown in 
        (None, {'fields': ('phone_number','email','full_name','password1','password2')}),
    )

    search_fields = ('email','full_name')
    ordering = ('full_name',)
    filter_horizontal = ()

admin.site.unregister(Group)           # to unregister django default used group 
admin.site.register(MyUser, UserAdmin)   # Our custom User model from models.py - Our custom User Admin from admin.py 

