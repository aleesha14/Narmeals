from django.contrib import admin

# Register your models here.
from .models import Meal, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday

admin.site.register(Meal)

admin.site.register(Monday)
admin.site.register(Tuesday)
admin.site.register(Wednesday)
admin.site.register(Thursday)
admin.site.register(Friday)
admin.site.register(Saturday)
admin.site.register(Sunday)

