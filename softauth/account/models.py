import string
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from utils import generator, security
from django.conf import settings
from django.utils import timezone


# User model and manager
class UserManager(BaseUserManager):
    '''User Manager Class'''
    def __create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        # generating uid and username
        uid = generator.generate_uuid()
        username = generator.generate_username(first_name, last_name)

        # creating user 
        user = self.model(uid=uid, email=self.normalize_email(email), first_name=first_name, last_name=last_name, username=username)

        # saving user with user password
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user_with_profile(self, first_name, last_name, gender, date_of_birth, msg_token, email, password=None):
        first_name = first_name.lower()
        last_name = last_name.lower()

        user = self.__create_user(email, first_name=first_name, last_name=last_name, password=password)

        # creating profile 
        user.gender = gender
        user.date_of_birth = date_of_birth

        # preparing user encryption key
        enc_key = generator.generate_password_key()
        aes = security.AES256(settings.SERVER_ENC_KEY)
        enc_key = aes.encrypt(enc_key)

        # setting user config
        user.enc_key = enc_key
        user.msg_token = msg_token
        user.is_signed = True
        user.is_active = True

        # saving user
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        first_name = first_name.lower()
        last_name = last_name.lower()

        user = self.__create_user(email, first_name=first_name, last_name=last_name, password=password)

        # setting admin user config
        user.is_signed = True
        user.is_active = True
        user.is_admin = True

        # saving user
        user.save(using=self._db)

        return user





# user model
class User(AbstractBaseUser):
    '''User Model Class'''
    uid = models.CharField(default=generator.generate_uuid(), max_length=36, unique=True, primary_key=True)
    first_name = models.CharField(default='', max_length=255)
    last_name = models.CharField(default='', max_length=255)
    email = models.EmailField(default='', max_length=255, unique=True)
    country_code = models.CharField(default='', max_length=10, blank=True)
    phone = models.CharField(default='', max_length=20, blank=True)
    username = models.CharField(default='', max_length=255, unique=True)
    gender = models.CharField(default='M', choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Others')), max_length=1)
    date_of_birth = models.CharField(default='', max_length=10, blank=True)
    photo = models.ImageField(upload_to='profile/photo')
    message = models.CharField(default='Hey there! I am using ChatDrop', blank=True, max_length=100)
    bio = models.CharField(default='', blank=True, max_length=2000)
    interest = models.TextField(default='', blank=True)
    website = models.CharField(default='', blank=True, max_length=1000)
    location = models.CharField(default='', blank=True, max_length=25)
    acc_type = models.CharField(default='ADMIN', choices=(('ADMIN', 'Admin'), ('DEPARTMENT', 'Department'), ('STUDENT', 'Student')), max_length=20)
    is_signed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    enc_key = models.TextField(default='', blank=True)
    msg_token = models.TextField(default='', blank=True)
    is_admin = models.BooleanField(default=False)
    terms_conditions = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.email} [ {self.uid} ]'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    @property
    def full_name(self) -> str:
        return string.capwords(f'{self.first_name} {self.last_name}')


# Login State
class LoginState(models.Model):
    '''Login State Model Class'''
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    token = models.CharField(default='', max_length=500)
    device = models.CharField(default='', max_length=20)
    os = models.CharField(default='', max_length=20)
    browser = models.CharField(default='', max_length=20)
    created_on = models.DateTimeField(default=None)
    active_until = models.DateTimeField(default=None)

    @property
    def is_active(self):
        return self.active_until >= timezone.now()