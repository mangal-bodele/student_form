from django.urls import path
from .views import add_student,show_student,update_student,delete_student

urlpatterns = [
    path('add/',add_student, name='add_url'),
    path('show/',show_student,name='show_url'),
    path('update/<int:pk>/',update_student,name='update_url'),
    path('delete/<int:pk>/',delete_student,name='delete_url')
]