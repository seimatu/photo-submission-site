from django.contrib import admin

# Register your models here.
from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display=('id','title')
    list_display_links=('id','title')

admin.site.register(Photo,PhotoAdmin)