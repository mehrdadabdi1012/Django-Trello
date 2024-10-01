from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import gettext as _

class MyUser(AbstractUser):
    """
    main user class
    """
    
    #----------------------------------------------
    # Choices Classes: 
    #----------------------------------------------
    class Work_Field_Choices(models.TextChoices):
        """
        choices for work_field
        """
        DEVELOPE   = 'DV', _('Develope')
        DEVOPS     = 'DO', _('Devops')
        DESIGN     = 'DS', _('Design')
        MARKETING  = 'MR', _('Marketing')
        MANAGEMENT = 'MN', _('Management')
        DATABASE   = 'DB', _('Database')


    class Work_Level_Choices(models.TextChoices):
        """
        choices for work_level
        """
        FRESHMAN = 'FR', _('Freshman')
        MIDDLE   = 'MD', _('Middle')
        JUNIOR   = 'JR', _('Junior')
        SENIOR   = 'SR', _('Senior')
        LEAD     = 'LD', _('Lead')


    #----------------------------------------------
    # Fields:
    #----------------------------------------------
    #id                 (from Default)
    #password           (from AbstractBaseUser)
    #last_login         (from AbstractBaseUser)
    #first_name         (from AbstractUser)
    #last_name          (from AbstractUser)
    #email              (from AbstractUser)
    #is_staff           (from AbstractUser)
    #is_active          (from AbstractUser)
    #date_joined        (from AbstractUser)
    phone_number = models.CharField(max_length=11, unique=True)
    birth_year = models.CharField(max_length=4)
    work_field = models.CharField(
        max_length=2,
        choices=Work_Field_Choices.choices,
    )
    work_level = models.CharField(
        max_length=2,
        choices=Work_Level_Choices.choices,
        default=Work_Level_Choices.FRESHMAN,
    )
    is_senior = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    #objects = UserManager()        (from AbstractUser)

    #EMAIL_FIELD = "email"          (from AbstractUser)
    #USERNAME_FIELD = "username"    (from AbstractUser)
    #REQUIRED_FIELDS = ["email"]    (from AbstractUser)
                                       
    REQUIRED_FIELDS = ['email']     # which fields must be given from user when use createsuperuser command
                                                # USERNAME_FIELD will be asked by default
                                                # then email will be asked
                                                # at the end password will be asked by default

    def __Str__(self):
        return self.email

    def has_perm(self, perm, obj=None):     # permissions
        return True

    def has_module_perms(self, app_label):   # permissions to other modules (models of which app)
        return True

    #@property
    #def is_staff(self):                     # can go to admin panel
        #return self.is_staff


#---------------------------------------------------------------------------------------------------------------------------
class RegularUser(models.Model):
    """
    class of regular users who join to teams
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='regularusers',
    )
    #id             (from Default)
    team_id = models.PositiveSmallIntegerField()

#---------------------------------------------------------------------------------------------------------------------------
class SeniorUser(models.Model):
    """
    class of senior users who create teams
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='seniorusers',
    )
    #id             (from Default)
    workspace_id = models.PositiveSmallIntegerField()



#in settings.py
#AUTH_USER_MODEL = 'accounts.MyUser'       # <appname>.<modelname>

