# exams/models.py

from django.db import models
from core.models import Program, Section
from django.contrib.auth import get_user_model
from rooms.models import Room

User = get_user_model()

class Exam(models.Model):
    EXAM_TYPE_CHOICES = [
        ('midterm', 'Midterm'),
        ('final', 'Final'),
    ]

    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    semester = models.PositiveIntegerField()

    course = models.CharField(max_length=255)
    exam_type = models.CharField(max_length=10, choices=EXAM_TYPE_CHOICES)
    date = models.DateField()
    time = models.TimeField()

    rooms = models.ManyToManyField(Room, blank=True)
    invigilators = models.ManyToManyField(User, blank=True, limit_choices_to={'user_type': 'faculty'})

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course} - {self.exam_type} ({self.date})"

    class Meta:
        ordering = ['date', 'time']
