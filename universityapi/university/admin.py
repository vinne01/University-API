from django.contrib import admin
#edit or customized admin panel

from university.models import University,Student,Teacher


#after write this code use python manage.py createsuperuser for authentic


class UniversityAdmin(admin.ModelAdmin):
    list_display=('name','location','type') 
    
    list_filter=('name',) 
 
class StudentAdmin(admin.ModelAdmin):
    list_display=('name','Roll_no','email')
    
    search_fields=('Roll_no',)

class TeacherAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','department')
    search_fields=('name','phone',)


admin.site.register(University,UniversityAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)

