from django.contrib import admin
from .models import Department, Student, Assignment


admin.site.register(Department)
admin.site.register(Assignment)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("username", "name", "email", "department", "year")
    search_fields = ("username", "name", "email")