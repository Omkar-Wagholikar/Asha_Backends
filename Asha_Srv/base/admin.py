from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(QueryLog)
admin.site.register(ErrorLog)
admin.site.register(FileModel)