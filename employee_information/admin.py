from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from employee_information.models import *

from django.contrib.auth.admin import UserAdmin, Group
from django.contrib.auth import admin as auth_admin





admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Employees)
admin.site.register(StatusEmployee)

admin.site.unregister(Group)
