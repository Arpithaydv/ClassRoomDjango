from django.contrib import admin

# Register your models here.
from django.contrib import admin
from enroll.models import Professor, Course, Student


class CourseAdmin(admin.ModelAdmin):
    field = ['course_name','student_name']


admin.site.register(Professor, CourseAdmin)
admin.site.register(Course)
admin.site.register(Student)

