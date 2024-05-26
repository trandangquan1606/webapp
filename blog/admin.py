from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date','id','audio','image']
    list_filter = ['date','title']
    search_fields=['title']
admin.site.register(Post, PostAdmin)