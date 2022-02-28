from django.urls import path
from . import views
  
urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_student_details, name='add-student-details'),
    path('all/', views.view_student_details, name='view_student_details'),
    path('update/<int:pk>/', views.update_details, name='update-details'),
    path('details/<int:pk>/delete/', views.delete_details, name='delete-details'),
    path('score/', views.ScoreApiOverview, name='home'),
    path('create-scorelist/', views.add_scorelist, name='add-student-score'),
    path('all-scorelist/', views.view_student_scorelist, name='view_student_score'),
    path('update-scorelist/<int:pk>/', views.update_scorelist, name='update-sorelist'),
    path('details-scorelist/<int:pk>/delete/', views.delete_scorelist, name='delete-scorelist'),
      
]