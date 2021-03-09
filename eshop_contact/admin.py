from django.contrib import admin
from .models import ContactUs


# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'subject', 'is_read']
    list_filter = ['is_read']


admin.site.register(ContactUs, ContactAdmin)
