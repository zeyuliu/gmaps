from django.db import models
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser

# Create your models here.

class WebUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=WebUserManager.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email,
            password=password,
            date_of_birth=date_of_birth
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class WebUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
        db_index=True,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = WebUserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['add required fields here']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return true
    # can view app 'app'
    def has_module_perms(self, app):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class UserProfile(models.Model):
    user = models.OneToOneField(User)
