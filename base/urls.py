from django.urls import path
from .views import CustomLoginView, DeleteView, Tasklist, TaskDetail, TaskCreate, TaskUpdate, RegisterPage
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns=[
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', Tasklist.as_view(), name = 'tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name = 'task'),
    path('task-create/', TaskCreate.as_view(), name = 'task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name = 'task-update'),
    path('task-delete/<int:pk>/',DeleteView.as_view(), name = 'task-delete'),
] 