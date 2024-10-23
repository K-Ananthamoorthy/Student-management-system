from django.db import models
from users.models import Student, Teacher

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='courses')
    students = models.ManyToManyField(Student, related_name='courses', blank=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='results')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='results')
    grade = models.CharField(max_length=2)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.course}: {self.grade}"

class Announcement(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_announcements')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_announcements')

    def __str__(self):
        return f"{self.course}: {self.title}"