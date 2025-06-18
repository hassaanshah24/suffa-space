# exams/admin.py

from django.contrib import admin
from .models import Exam

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('course', 'exam_type', 'program', 'section', 'semester', 'date', 'time')
    list_filter = ('exam_type', 'program', 'semester', 'date')
    search_fields = ('course',)
    filter_horizontal = ('rooms', 'invigilators')
    ordering = ('date', 'time')
    date_hierarchy = 'date'
