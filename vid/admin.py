from django.contrib import admin

from .models import Blog, BlogComment, Contact, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(BlogComment)
