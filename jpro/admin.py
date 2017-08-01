from django.contrib import admin
from .models import Post
from .models import Tournaments
from .models import tennisinfo
# Register your models here.

admin.site.register(Post)
admin.site.register(Tournaments)
admin.site.register(tennisinfo)
