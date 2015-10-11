from django.contrib import admin
from bots.models import Bot, Log, Author

# Register your models here.
admin.site.register(Bot)
admin.site.register(Log)
admin.site.register(Author)