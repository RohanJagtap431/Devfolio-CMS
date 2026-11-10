from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom user model for Devfolio CMS.
    Only the site owner will have admin access.
    """

    class Meta:
        verbose_name = "Admin User"
        verbose_name_plural = "Admin Users"