from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


# Create User Ability to register and login with email.
# No username is required. I overwrote the UserManage and inherited
# from BaseUserManager to create my own model manager for user with no
# username field.
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


# Created my own User model by inheriting from AbstractUser.
# This User model is the base user class for each type of user. A role field
# is defined also so I can easily track what each user is and their permissions
class User(AbstractUser):

    username = None
    company_name = models.CharField(max_length=200, default='Company Name')     
    email = models.EmailField(_('email address'), unique=True)
    employee_number = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    admin = models.BooleanField(default=True)
    employee_phone = models.IntegerField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='upload_pics/', unique=False,
                                      blank=True, null=True,
                                      default='static/images/profile-placeholder.png')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['employee_number', 'admin', 'employee_phone',
                       'birth_date', 'profile_image']

    objects = UserManager()

    def __str__(self):
        return "{} {} - Employee #: {}".format(self.first_name,
                                               self.last_name,
                                               self.employee_number)

class Employee(User):
    boss = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='employee_boss')
