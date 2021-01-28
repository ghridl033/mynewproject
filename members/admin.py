from django.contrib import admin
from .models import Members
# Register your models here.
class MembersAdmin(admin.ModelAdmin):
    list_display = ('username','useremail','password')
    pass

admin.site.register(Members, MembersAdmin)
