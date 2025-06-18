from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Exam
from .forms import ExamForm

def is_admin(user):
    return user.is_superuser

def is_faculty(user):
    return user.user_type == 'faculty'

@login_required
def exam_list_view(request):
    exams = Exam.objects.all().order_by('date', 'time')
    context = {
        'exams': exams,
    }
    return render(request, 'exams/exam_list.html', context)

@login_required
@user_passes_test(is_admin)
def exam_create_view(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Exam created successfully!')
            return redirect('exams:exam_list')
    else:
        form = ExamForm()

    context = {
        'form': form,
    }
    return render(request, 'exams/exam_form.html', context)

@login_required
def my_exam_schedule_view(request):
    user = request.user
    if user.user_type == 'faculty':
        exams = Exam.objects.filter(invigilators=user).order_by('date', 'time')
    elif user.user_type == 'student':
        exams = Exam.objects.filter(
            program=user.program,
            section=user.section,
            semester=user.semester
        ).order_by('date', 'time')
    else:
        exams = Exam.objects.none()

    context = {
        'exams': exams,
    }
    return render(request, 'exams/my_exam_schedule.html', context)
