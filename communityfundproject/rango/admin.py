from django.contrib import admin
from rango.models import Category, Page
from rango.models import RangoUserProfile

# Update the registeration to include this customised interface
admin.site.register(Category)
admin.site.register(Page)
admin.site.register(RangoUserProfile)