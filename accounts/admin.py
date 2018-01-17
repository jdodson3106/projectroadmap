from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import User, Employee

# This creates the admin model for the customer User model I created so that
# admin does not require username field. This essentially customizes what I will
# see reglected in the admin page
@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no username field."""

    fieldsets = (
        (None, {'fields': ('company_name','employee_number','email', 'password')}),
        (_('Personal info'), {'fields': ('first_name','last_name',
                                         'employee_phone', 'birth_date', 'profile_image')}),
        (_('Permissions'), {'fields': ('is_active', 'admin', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('company_name','employee_number', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('employee_number','email',
                    'first_name', 'last_name',
                    'admin','is_staff')
    search_fields = ('employee_number','email', 'first_name', 'last_name')
    ordering = ('email',)

# register the profiles so I can view them in the admin page
admin.site.register(Employee)
