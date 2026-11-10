
from django.db import models


class PortfolioProfile(models.Model):

    # Personal Information
    full_name = models.CharField(max_length=150)
    professional_title = models.CharField(max_length=200)

    profile_photo = models.ImageField(
        upload_to="portfolio/profile/",
        blank=True,
        null=True
    )

    short_bio = models.TextField()
    about_me = models.TextField(blank=True)

    # Contact Information
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=150, blank=True)

    # Social Links
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)

    # Resume
    resume = models.FileField(
        upload_to="portfolio/resume/",
        blank=True,
        null=True
    )

    # Availability
    is_available_for_work = models.BooleanField(default=True)

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Portfolio Profile"
        verbose_name_plural = "Portfolio Profile"

    def __str__(self):
        return self.full_name
