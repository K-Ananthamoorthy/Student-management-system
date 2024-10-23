from django import forms
from users.models import Student, User
from courses.models import Result, Announcement

class StudentForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.filter(user_type=1), label="User")

    class Meta:
        model = Student
        fields = ['user', 'student_id', 'date_of_birth']

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['grade', 'score']

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content']