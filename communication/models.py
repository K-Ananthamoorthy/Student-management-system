# from django.db import models
# from users.models import User
# from courses.models import Course

# class Announcement(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='announcements')
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title