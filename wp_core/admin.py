from django.contrib import admin
from wp_core.models import *

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(VoteQuestion)
admin.site.register(VoteAnswer)
admin.site.register(Tag)
admin.site.register(Userprofile)



