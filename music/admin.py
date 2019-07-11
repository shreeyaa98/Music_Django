from django.contrib import admin
from .models import Album,Song

# Register your models here. So that they can be changed from admin page

admin.site.register(Album)
admin.site.register(Song)