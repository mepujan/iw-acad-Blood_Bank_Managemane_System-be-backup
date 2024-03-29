from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

gender = (('male', 'male'), ('female', 'female'), ('others', 'others'))
status = (('donor', 'donor'), ('seeker', 'seeker'))
blood_type = (
    ('O+', 'O-Positive'), ('O-', 'O-Negative'), ('A+', 'A-Positive'), ('A-', 'A-Negative'), ('B+', 'B-Positive'),
    ('B-', 'B-Negative'), ('AB+', 'AB-Positive'), ('AB-', 'AB-Negative'))


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    address = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    DOB = models.DateField(null=True)
    gender = models.CharField(max_length=6, choices=gender)
    status = models.CharField(max_length=6, choices=status)
    blood_group = models.CharField(max_length=15, choices=blood_type)
    created_at = models.DateField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='profile')
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('active'), default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name
