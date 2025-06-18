# core/models.py

from django.db import models

class Program(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, unique=True)
    duration_years = models.PositiveIntegerField(default=4)

    def __str__(self):
        return f"{self.code} - {self.name}"

class Section(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='sections')
    name = models.CharField(max_length=10)  # e.g., A, B, C
    semester = models.PositiveIntegerField(default=1)
    academic_year = models.CharField(max_length=9)  # e.g., 2024-2025

    def __str__(self):
        return f"{self.program.code} - Sem {self.semester} - Sec {self.name} ({self.academic_year})"
