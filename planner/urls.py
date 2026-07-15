from django.urls import path
from . import views

# App-level routing namespacing to reference URLs dynamically in templates
app_name = 'planner'

urlpatterns = [
    path('', views.home, name='home'),               # Route for homepage: /
    path('about/', views.about, name='about'),       # Route for about page: /about/
    path('contact/', views.contact, name='contact'), # Route for contact page: /contact/
    
    # Authentication Routes
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Task CRUD Routes
    path('tasks/', views.tasks_list, name='tasks_list'),
    path('tasks/add/', views.task_add, name='task_add'),
    path('tasks/complete/', views.task_complete, name='task_complete'),
    path('tasks/delete/', views.task_delete, name='task_delete'),
    
    # Event CRUD Routes
    path('events/', views.events_list, name='events_list'),
    path('events/add/', views.event_add, name='event_add'),
    path('events/delete/', views.event_delete, name='event_delete'),
]
