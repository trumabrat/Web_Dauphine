from django.contrib import admin
from .models import Person, Quote

# Register your models here.
admin.site.register(Person)
admin.site.register(Quote)