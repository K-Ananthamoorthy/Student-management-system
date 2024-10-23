from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('student/', views.student_dashboard, name='student_dashboard'),
    path('teacher/', views.teacher_dashboard, name='teacher_dashboard'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('add_student/', views.add_student, name='add_student'),
    path('edit_student/<str:student_id>/', views.edit_student, name='edit_student'),
    path('course/<int:course_id>/add_student/', views.add_student_to_course, name='add_student_to_course'),
    path('course/<int:course_id>/student/<str:student_id>/add_result/', views.add_result, name='add_result'),
    path('edit_result/<int:result_id>/', views.edit_result, name='edit_result'),
    path('course/<int:course_id>/create_announcement/', views.create_announcement, name='create_announcement'),
]