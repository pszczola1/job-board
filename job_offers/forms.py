from django import forms
from .models import JobListing

class JobListingCreationForm(forms.ModelForm):
    class Meta():
        model = JobListing
        fields = ['title', 'categories', 'description', 'offered_pay']
        widgets = {
            'categories': forms.CheckboxSelectMultiple()
        }
