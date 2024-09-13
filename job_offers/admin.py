from django.contrib import admin
from .models import Category, JobListing

# Register your models here.

admin.site.register(Category)
admin.site.register(JobListing)