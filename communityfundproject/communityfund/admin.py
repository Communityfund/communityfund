from django.contrib import admin
from communityfund.models import Communities, Usernames, CommunityProjects, Interests, UserProfile, CommunityProject, Payment, Comment, ProjectComment, UserInterest

admin.site.register(Communities)
#admin.site.register(Usernames)
#admin.site.register(CommunityProjects)
admin.site.register(CommunityProject)
admin.site.register(Interests)
admin.site.register(UserProfile)
admin.site.register(Payment)
admin.site.register(Comment)
admin.site.register(ProjectComment)
admin.site.register(UserInterest)
# Register your models here.
