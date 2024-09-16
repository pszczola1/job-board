from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import JobListingCreationForm
from .models import JobListing

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

def listings(request):
    page_number = request.GET.get("page")

    listings = JobListing.objects.all()
    paginator = Paginator(listings, 10)
    page_obj = paginator.get_page(page_number)
    return render(request, "job_offers/listings.html", {'page_obj': page_obj})

def listing(request, id):
    ...