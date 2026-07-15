from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    """
    A custom registration form that extends Django's UserCreationForm
    to include an email field and apply Bootstrap styling.
    """
    email = forms.EmailField(required=True, label="Email Address")

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        # Apply Bootstrap's form-control class to all inputs dynamically
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

from .models import Task

class TaskForm(forms.ModelForm):
    """
    Form to create and edit Tasks. Bound to the Task model.
    """
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        # Dynamically apply Bootstrap classes to all inputs
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'

from .models import Event

class EventForm(forms.ModelForm):
    """
    Form to create and edit Events. Bound to the Event model.
    """
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'start_time', 'end_time', 'location']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # Dynamically apply Bootstrap classes to all inputs
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'
