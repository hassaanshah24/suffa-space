# exams/forms.py

from django import forms
from .models import Exam

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = [
            'program', 'section', 'semester',
            'course', 'exam_type', 'date', 'time',
            'rooms', 'invigilators'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'rooms': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'invigilators': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }
