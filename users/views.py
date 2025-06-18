from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserForm
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

# PROFILE VIEW
@login_required
def profile_view(request):
    user = request.user  # this is already CustomUser

    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('users:profile')
    else:
        form = CustomUserForm(instance=user)

    context = {
        'form': form,
    }

    return render(request, 'users/profile.html', context)

# LOGIN REDIRECT
@login_required
def login_redirect_view(request):
    user = request.user

    if user.is_superuser:
        return redirect('users:admin_dashboard')
    elif user.user_type == 'faculty':
        return redirect('users:faculty_dashboard')
    elif user.user_type == 'student':
        return redirect('users:student_dashboard')
    else:
        # fallback
        messages.error(request, "Unknown user type. Please contact admin.")
        return redirect('users:profile')

# ADMIN DASHBOARD
@login_required
def admin_dashboard(request):
    total_users = User.objects.count()
    admins = User.objects.filter(is_staff=True).count()
    students = User.objects.filter(user_type='student').count()

    context = {
        'total_users': total_users,
        'admins': admins,
        'students': students,
    }

    return render(request, 'users/admin_dashboard.html', context)

# FACULTY DASHBOARD
@login_required
def faculty_dashboard(request):
    if request.user.user_type != 'faculty':
        return redirect('users:dashboard')

    # Dummy Data
    booked_rooms = [
        {'room': 'A-201', 'date': 'June 20', 'time': '10:00 - 12:00'},
        {'room': 'B-105', 'date': 'June 21', 'time': '14:00 - 16:00'},
    ]

    invigilator_duties = [
        {'course': 'CS101 Midterm', 'date': 'June 25', 'room': 'C-301'},
        {'course': 'MTH202 Final', 'date': 'July 2', 'room': 'A-101'},
    ]

    notifications = [
        'System maintenance scheduled on June 24.',
        'New classroom Lab-5 is now available.',
    ]

    context = {
        'booked_rooms': booked_rooms,
        'invigilator_duties': invigilator_duties,
        'notifications': notifications,
    }

    return render(request, 'users/faculty_dashboard.html', context)

# STUDENT DASHBOARD
@login_required
def student_dashboard(request):
    if request.user.user_type != 'student':
        return redirect('users:login_redirect_view')

    upcoming_exams = [
        {'course': 'CS101', 'date': '2025-06-26', 'room': 'C-302', 'seat': 'A12'},
        {'course': 'ENG201', 'date': '2025-07-03', 'room': 'B-102', 'seat': 'B15'},
    ]

    notifications = [
        'Midterm exams start from June 25.',
        'Bring your ID Card for all exams.',
    ]

    context = {
        'upcoming_exams': upcoming_exams,
        'notifications': notifications,
    }

    return render(request, 'users/student_dashboard.html', context)
