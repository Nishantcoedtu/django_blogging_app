from django.contrib import admin
from .models import Category, Post
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','url','add_date')
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','content','url','cat')
    search_fields =('title',)
    list_filter = ('cat',)

    class Media:
        js=('js/script.js',)


admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
