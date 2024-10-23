from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from users.models import User, Student, Teacher
from courses.models import Course, Result, Announcement
from .forms import StudentForm, ResultForm, AnnouncementForm

# ... (rest of the file remains the same)
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.user_type == 1:  # Student
                return redirect('student_dashboard')
            elif user.user_type == 2:  # Teacher
                return redirect('teacher_dashboard')
            else:
                return redirect('admin:index')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def is_teacher(user):
    return user.user_type == 2

@login_required
@user_passes_test(is_teacher)
def teacher_dashboard(request):
    teacher = request.user.teacher
    courses = Course.objects.filter(teacher=teacher)
    return render(request, 'core/teacher_dashboard.html', {'courses': courses})

@login_required
@user_passes_test(is_teacher)
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id, teacher=request.user.teacher)
    students = course.students.all()
    results = Result.objects.filter(course=course)
    announcements = Announcement.objects.filter(course=course)
    return render(request, 'core/course_detail.html', {
        'course': course,
        'students': students,
        'results': results,
        'announcements': announcements
    })

@login_required
@user_passes_test(is_teacher)
def add_student_to_course(request, course_id):
    course = get_object_or_404(Course, id=course_id, teacher=request.user.teacher)
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        student = get_object_or_404(Student, student_id=student_id)
        course.students.add(student)
        messages.success(request, f'{student} added to {course}')
        return redirect('course_detail', course_id=course.id)
    return render(request, 'core/add_student_to_course.html', {'course': course})

@login_required
@user_passes_test(is_teacher)
def edit_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, f'Student {student} updated successfully')
            return redirect('course_detail', course_id=request.POST.get('course_id'))
    else:
        form = StudentForm(instance=student)
    return render(request, 'core/edit_student.html', {'form': form, 'student': student})

@login_required
@user_passes_test(lambda u: u.user_type == 2)  # Ensure only teachers can access this view
def add_result(request, course_id, student_id):
    course = get_object_or_404(Course, id=course_id, teacher=request.user.teacher)
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.course = course
            result.student = student
            result.save()
            messages.success(request, f'Result added for {student.user.get_full_name()} in {course.name}')
            return redirect('course_detail', course_id=course.id)
    else:
        form = ResultForm()
    return render(request, 'core/add_result.html', {'form': form, 'course': course, 'student': student})

@login_required
@user_passes_test(is_teacher)
def create_announcement(request, course_id):
    course = get_object_or_404(Course, id=course_id, teacher=request.user.teacher)
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.course = course
            announcement.created_by = request.user.teacher
            announcement.save()
            messages.success(request, 'Announcement created successfully')
            return redirect('course_detail', course_id=course.id)
    else:
        form = AnnouncementForm()
    return render(request, 'core/create_announcement.html', {'form': form, 'course': course})

@login_required
def student_dashboard(request):
    student = request.user.student
    courses = student.courses.all()
    results = Result.objects.filter(student=student)
    announcements = Announcement.objects.filter(course__in=courses).order_by('-created_at')[:5]
    return render(request, 'core/student_dashboard.html', {
        'student': student,
        'courses': courses,
        'results': results,
        'announcements': announcements,
    })




# ... (keep existing views)

@login_required
@user_passes_test(is_teacher)
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'New student {student.user.get_full_name()} added successfully')
            return redirect('teacher_dashboard')
    else:
        form = StudentForm()
    return render(request, 'core/add_student.html', {'form': form})

@login_required
@user_passes_test(is_teacher)
def edit_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, f'Student {student.user.get_full_name()} updated successfully')
            return redirect('teacher_dashboard')
    else:
        form = StudentForm(instance=student)
    return render(request, 'core/edit_student.html', {'form': form, 'student': student})

@login_required
@user_passes_test(is_teacher)
def add_result(request, course_id, student_id):
    course = get_object_or_404(Course, id=course_id, teacher=request.user.teacher)
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.course = course
            result.student = student
            result.save()
            messages.success(request, f'Result added for {student.user.get_full_name()} in {course.name}')
            return redirect('course_detail', course_id=course.id)
    else:
        form = ResultForm()
    return render(request, 'core/add_result.html', {'form': form, 'course': course, 'student': student})

@login_required
@user_passes_test(is_teacher)
def edit_result(request, result_id):
    result = get_object_or_404(Result, id=result_id, course__teacher=request.user.teacher)
    if request.method == 'POST':
        form = ResultForm(request.POST, instance=result)
        if form.is_valid():
            form.save()
            messages.success(request, f'Result updated for {result.student.user.get_full_name()} in {result.course.name}')
            return redirect('course_detail', course_id=result.course.id)
    else:
        form = ResultForm(instance=result)
    return render(request, 'core/edit_result.html', {'form': form, 'result': result})

@login_required
@user_passes_test(is_teacher)
def create_announcement(request, course_id):
    course = get_object_or_404(Course, id=course_id, teacher=request.user.teacher)
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.course = course
            announcement.created_by = request.user.teacher
            announcement.save()
            messages.success(request, 'Announcement created successfully')
            return redirect('course_detail', course_id=course.id)
    else:
        form = AnnouncementForm()
    return render(request, 'core/create_announcement.html', {'form': form, 'course': course})