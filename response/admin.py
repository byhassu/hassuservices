from django.contrib import admin
from response.models import responseForm
from django.contrib.admin.sites import site
class responseAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','desc')
admin.site.register(responseForm,responseAdmin)

# Register your models here.
