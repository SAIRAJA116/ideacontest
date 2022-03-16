from atexit import register
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(ProminentParameter)
admin.site.register(AtmosCondition)
admin.site.register(PondCondition)
admin.site.register(Combinations)
