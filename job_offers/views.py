from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.serializers import serialize
from .forms import JobListingCreationForm, JobListingFilterForm
from .models import JobListing

# Create your views here.

def home(request):
    return render(request, "core/home.html")

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

def listings(request):
    filter_form = JobListingFilterForm()
    return render(request, "job_offers/listings.html", {'form': filter_form})

def listing(request, pk):
    listing_obj = JobListing.objects.get(pk=pk)
    return render(request, "job_offers/listing.html", {"listing": listing_obj})