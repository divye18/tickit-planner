from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import UserRegisterForm, TaskForm, EventForm
from .models import Task, Event

# Existing Landing Views
def home(request):
    """
    Renders the PlanPilot Homepage.
    If the user is already authenticated, redirect them to the dashboard.
    """
    if request.user.is_authenticated:
        return redirect('planner:dashboard')
    return render(request, 'planner/index.html')

def about(request):
    """
    Renders the About Page for PlanPilot.
    """
    return render(request, 'planner/about.html')

def contact(request):
    """
    Renders the Contact Page for PlanPilot.
    """
    return render(request, 'planner/contact.html')

# Authentication Views
def register(request):
    """
    Handles user registration.
    """
    if request.user.is_authenticated:
        return redirect('planner:dashboard')
        
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('planner:dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'planner/register.html', {'form': form})

def login_view(request):
    """
    Handles user login.
    """
    if request.user.is_authenticated:
        return redirect('planner:dashboard')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('planner:dashboard')
    else:
        form = AuthenticationForm()
        
    for field_name, field in form.fields.items():
        field.widget.attrs['class'] = 'form-control'
        
    return render(request, 'planner/login.html', {'form': form})

def logout_view(request):
    """
    Logs out the user and redirects to the homepage.
    """
    auth_logout(request)
    return redirect('planner:home')

# Live Dashboard View
@login_required
def dashboard(request):
    """
    Renders the dashboard with live data from the SQLite database.
    """
    today = timezone.now().date()
    pending = Task.objects.filter(user=request.user, completed=False)
    completed = Task.objects.filter(user=request.user, completed=True)
    
    pending_count = pending.count()
    completed_count = completed.count()
    total_count = pending_count + completed_count
    
    completion_percentage = int((completed_count / total_count) * 100) if total_count > 0 else 0
    
    context = {
        'pending_tasks_count': pending_count,
        'completed_tasks_count': completed_count,
        'upcoming_events_count': Event.objects.filter(user=request.user, date__gte=today).count(),
        'total_events_count': Event.objects.filter(user=request.user).count(),
        'completion_percentage': completion_percentage,
        'recent_tasks': pending.order_by('due_date')[:3],
        'recent_events': Event.objects.filter(user=request.user, date__gte=today).order_by('date', 'start_time')[:3],
    }
    return render(request, 'planner/dashboard.html', context)

# Task CRUD Views
@login_required
def tasks_list(request):
    """
    Lists the logged-in user's pending and completed tasks.
    """
    tasks = Task.objects.filter(user=request.user).order_by('due_date')
    pending_tasks = tasks.filter(completed=False)
    completed_tasks = tasks.filter(completed=True)
    
    return render(request, 'planner/tasks_list.html', {
        'pending_tasks': pending_tasks,
        'completed_tasks': completed_tasks,
    })

@login_required
def task_add(request):
    """
    Renders a form to add a new task and saves it to the database.
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Securely associate task with logged-in user
            task.save()
            return redirect('planner:tasks_list')
    else:
        form = TaskForm()
    return render(request, 'planner/task_add.html', {'form': form})

@login_required
def task_complete(request):
    """
    Retrieves a task by ID (verifying user ownership) and marks it as complete.
    Uses POST check or simple URL trigger. We'll handle a direct GET redirect.
    """
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, id=task_id, user=request.user)
        task.completed = True
        task.save()
    return redirect('planner:tasks_list')

@login_required
def task_delete(request):
    """
    Retrieves a task by ID (verifying user ownership) and deletes it.
    """
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, id=task_id, user=request.user)
        task.delete()
    return redirect('planner:tasks_list')

# Event CRUD Views
@login_required
def events_list(request):
    """
    Lists the logged-in user's events sorted chronologically.
    """
    events = Event.objects.filter(user=request.user).order_by('date', 'start_time')
    return render(request, 'planner/events_list.html', {'events': events})

@login_required
def event_add(request):
    """
    Renders a form to add a new event and saves it to the database.
    """
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user  # Securely associate event with logged-in user
            event.save()
            return redirect('planner:events_list')
    else:
        form = EventForm()
    return render(request, 'planner/event_add.html', {'form': form})

@login_required
def event_delete(request):
    """
    Retrieves an event by ID (verifying user ownership) and deletes it.
    """
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        event = get_object_or_404(Event, id=event_id, user=request.user)
        event.delete()
    return redirect('planner:events_list')

@login_required
def calendar_view(request):
    """
    Renders the Calendar View displaying the user's scheduled events.
    """
    import json
    events = Event.objects.filter(user=request.user)
    events_data = []
    for event in events:
        start_datetime = f"{event.date.isoformat()}T{event.start_time.isoformat()}"
        end_datetime = f"{event.date.isoformat()}T{event.end_time.isoformat()}"
        events_data.append({
            'id': event.id,
            'title': event.title,
            'start': start_datetime,
            'end': end_datetime,
            'description': event.description,
            'location': event.location,
            'start_time': event.start_time.strftime("%I:%M %p"),
            'end_time': event.end_time.strftime("%I:%M %p"),
            'date': event.date.strftime("%B %d, %Y"),
        })
    context = {
        'events_json': json.dumps(events_data)
    }
    return render(request, 'planner/calendar.html', context)
