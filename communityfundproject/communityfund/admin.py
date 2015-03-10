from django.contrib import admin
from communityfund.models import Communities, Usernames, CommunityProjects, Interest

admin.site.register(Communities)
admin.site.register(Usernames)
admin.site.register(CommunityProjects)
admin.site.register(Interest)

# Register your models here.
