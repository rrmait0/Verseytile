from django.contrib import admin
from .models import Forum, Discussion

# Register your models here.

class Forum_admin(admin.ModelAdmin):
    fields=[

        'title',
        'subtitle',
        'slug',
        'published',
        'author',
        'image',
    ]

class Discussion_admin(admin.ModelAdmin):
    fieldsets =[
        ("Header",{"fields": ['title','subtitle','Discussion_slug','a_forum','author','image']}),
        ("Content", {"fields" : ['content','notes']}),
        ("Date",{"fields" : ['modified']}),
        


    ]

admin.site.register(Forum, Forum_admin)
admin.site.register(Discussion,Discussion_admin)
