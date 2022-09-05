from atexit import register
from django.contrib import admin
from base.models import *
# Register your models here.
admin.site.register(Signup)
admin.site.register(MyUser)