# exams/urls.py

from django.urls import path
from . import views

app_name = 'exams'

urlpatterns = [

    # Admin/Faculty — View All Exams
    path('list/', views.exam_list_view, name='exam_list'),

    # Admin/Faculty — Add Exam
    path('add/', views.exam_create_view, name='exam_add'),

    # Student — My Exam Schedule (calendar + seat plan)
    path('my-schedule/', views.my_exam_schedule_view, name='my_exam_schedule'),

]
