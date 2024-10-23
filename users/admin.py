from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Student, Teacher
from courses.models import Course, Result, Announcement

# ... (rest of the file remains the same)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'first_name', 'last_name', 'user_type', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('user_type',)}),
    )

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'teacher']
    search_fields = ['name', 'code', 'teacher__user__username']

class ResultAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'grade', 'score', 'date']
    list_filter = ['course', 'date']
    search_fields = ['student__user__username', 'course__name']

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'created_by', 'created_at']
    list_filter = ['course', 'created_at']
    search_fields = ['title', 'content', 'course__name']

admin.site.register(User, CustomUserAdmin)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course, CourseAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Announcement, AnnouncementAdmin)