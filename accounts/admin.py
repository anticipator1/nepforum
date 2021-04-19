from django.contrib import admin

# Register your models here.
from .models import Forum_Users,Post,AddComment

admin.site.register(Forum_Users)
admin.site.register(Post)
admin.site.register(AddComment)