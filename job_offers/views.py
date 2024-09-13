from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import JobListingCreationForm

# Create your views here.

def create_listing(request):
    if request.method == "POST":
        form = JobListingCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, "Created")
            return redirect("/")
    form = JobListingCreationForm()
    context = {"form": form}
    return render(request, "job_offers/create_listing.html", context=context)

def listing(request, id):
    ...