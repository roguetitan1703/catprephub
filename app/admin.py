from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(TestSection)
admin.site.register(Question)
admin.site.register(TestResult)