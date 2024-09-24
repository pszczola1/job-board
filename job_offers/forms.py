from django import forms
from .models import JobListing

class JobListingCreationForm(forms.ModelForm):
    class Meta():
        model = JobListing
        fields = ['title', 'categories', 'description', 'salary']
        widgets = {
            'categories': forms.CheckboxSelectMultiple()
        }

class JobListingFilterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs): # all fields are required by default
        super().__init__(*args, **kwargs)
        self.fields['salary'].initial = 0
        for field in self.fields.values():
            field.required = False

    class Meta():
        model = JobListing
        fields = ['title', 'categories', 'salary', 'location', 'employment_type', 'work_model']
        required = []
        widgets = {
            'categories': forms.CheckboxSelectMultiple(),
            'employment_type': forms.CheckboxSelectMultiple(),
            'work_model': forms.CheckboxSelectMultiple()
        }