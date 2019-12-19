from django.contrib import admin

# Register your models here.
from .models import Category,Photo

class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','title')
    list_display=('id','title')

class PhotoAdmin(admin.ModelAdmin):
    list_display=('id','title')
    list_display_links=('id','title')

admin.site.register(Photo,PhotoAdmin)
admin.site.register(Category,CategoryAdmin)