from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomUserManager

# Create your models here.

class User(AbstractBaseUser):
    # fields
    email = models.EmailField("Email adress", max_length=255, unique=True)
    first_name = models.CharField("First name", max_length=63)
    last_name = models.CharField("Last name", max_length=63)
    date_joined = models.DateField(auto_now_add=True)
    date_of_birth = models.DateField("Date of birth")
    #profile_image = models.ImageField()

    #https://stackoverflow.com/questions/62504785/typeerror-user-got-an-unexpected-keyword-argument-is-staff-when-using-custo
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    #"email" is also required
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "date_of_birth"]

    objects = CustomUserManager()

    def __str__(self) -> str:
        return f"{self.email} {self.first_name} {self.last_name}"
    

    #https://stackoverflow.com/questions/31370333/custom-django-user-object-has-no-attribute-has-module-perms
    def has_perm(self, perm, obj=None):
        return self.is_superuser
    
    def has_module_perms(self, app_label):
        return self.is_superuser
    