from django.contrib import admin
from .models import COntact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','message')
    list_display_link = ('id', 'name')
    search_fields = ('name','email','subject')
    list_per_page = 25

admin.site.register(COntact, ContactAdmin)