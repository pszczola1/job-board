from django.db import models
from django_quill.fields import QuillField

# Create your models here.

class Category(models.Model):
    # CATEGORY_CHOICES  = [
    #     ('banking', 'Banking'),
    #     ('education', 'Education'),
    #     ('IT', 'IT'),
    #     ('law', 'Law'),
    #     ('sales', 'Sales'),
    #     ('real_estate', 'Real Estate'),
    #     ('human_resouroces', 'Human Resouroces'),
    #     ('logistics', 'Logistics'),
    #     ('customer_service', 'Customer Service'),
    #     ('art', 'Art'),
    #     # more will be added later
    # ]
    # name = models.CharField(choices=CATEGORY_CHOICES, max_length=127)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=127, unique=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class JobListing(models.Model):
    title = models.CharField(max_length=511, null=False)
    categories = models.ManyToManyField(Category)
    #listing_image = models.ImageField(verbose_name="listing_image")
    description = QuillField(verbose_name="description")
    salary = models.IntegerField(verbose_name="salary", default=5000)

    def __str__(self) -> str:
        #format: title(up to ten characters) and the id of the object in []
        text = (f"{self.title[:10]}..." if len(self.title) > 10 else f"{self.title[:10]}") + f" [{self.pk}]" 
        return text
