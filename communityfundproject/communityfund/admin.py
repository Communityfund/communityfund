from django.contrib import admin
from communityfund.models import Communities, Users, Projects, Interests

admin.site.register(Communities)
admin.site.register(communityfund.models.Users)
admin.site.register(communityfund.models.Projects)
admin.site.register(Interests)

# Register your models here.
