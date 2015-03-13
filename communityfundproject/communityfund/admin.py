from django.contrib import admin
from communityfund.models import Communities, Usernames, CommunityProjects, Interests, UserProfile

admin.site.register(Communities)
admin.site.register(Usernames)
admin.site.register(CommunityProjects)
admin.site.register(Interests)
admin.site.register(UserProfile)
# Register your models here.
