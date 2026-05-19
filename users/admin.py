from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile

admin.site.register(Profile)

from .models import Internship

admin.site.register(Internship)

from .models import Application

admin.site.register(Application)