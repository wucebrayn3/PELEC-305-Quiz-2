from .models import EventRegistration
from django import forms

class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = ['full_name', 'email', 'age', 'password']
        
    def clean_name(self):
        name = self.cleaned_data.get('full_name')
        if not name:
            raise forms.ValidationError("Full name is required.")
        
        if len(name) < 5:
            raise forms.ValidationError("Full name must be at least 5 characters long.")
        
        return name
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required.")
        
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Email must be a valid Gmail address.")
        
        return email
    
    def clean_age(self):
        age = self.cleaned_data.get('age')
        
        if age is None:
            raise forms.ValidationError("Age is required.")
        
        if age < 18:
            raise forms.ValidationError("You must be at least 18 years old to register.")
        
        return age
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        
        if not password:
            raise forms.ValidationError("Password is required.")
        
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        
        return password