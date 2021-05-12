from django.contrib import admin
from jobs.models import Job

#定义JobAdmin类以便添加显示列表和显示项
class JobAdmin(admin.ModelAdmin):
    exclude = ('creator','create_time','modified_time')
    list_display = ('job_type','job_name','job_city','creator','create_time','modified_time')

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)



# Register your models here.
admin.site.register(Job,JobAdmin)
