from django.contrib import admin
from .models import morning_entry, evening_entry, anchor
# Register your models here.

admin.site.register(morning_entry)
admin.site.register(evening_entry)
admin.site.register(anchor)