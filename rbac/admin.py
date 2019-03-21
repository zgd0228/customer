from django.contrib import admin
from rbac.models import *
# Register your models here.

admin.site.register(Permission)
admin.site.register(Role)
admin.site.register(UserInfo)
admin.site.register(Menu)