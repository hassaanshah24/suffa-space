# core/admin.py

from django.contrib import admin
from .models import Program, Section

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'duration_years')
    search_fields = ('name', 'code')

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('program', 'name', 'semester', 'academic_year')
    list_filter = ('program', 'semester', 'academic_year')
