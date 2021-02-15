from django.contrib import admin
from .models import Department,Profile,Post
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    filter_horizontal =('department',)

admin.site.register(Department)
admin.site.register(Profile)
admin.site.register(Post)