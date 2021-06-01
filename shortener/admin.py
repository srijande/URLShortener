from django.contrib import admin

# Register your models here.

from .models import Shortener

class OrganizerAdmin(admin.ModelAdmin):
   
    fields = ('original_link', 'shortened_link', 'created')


admin.site.register(Shortener,OrganizerAdmin)