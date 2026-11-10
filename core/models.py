
from django.db import models


class SiteSettings(models.Model):

    # Website Information
    site_name = models.CharField(
        max_length=150,
        default="Devfolio"
    )

    tagline = models.CharField(
        max_length=250,
        blank=True
    )

    footer_text = models.CharField(
        max_length=250,
        blank=True
    )

    # SEO Settings
    meta_title = models.CharField(
        max_length=200,
        blank=True
    )

    meta_description = models.TextField(
        max_length=320,
        blank=True
    )

    meta_keywords = models.CharField(
        max_length=500,
        blank=True
    )

    # Website Images
    favicon = models.ImageField(
        upload_to="portfolio/settings/",
        blank=True,
        null=True
    )

    og_image = models.ImageField(
        upload_to="portfolio/settings/",
        blank=True,
        null=True
    )

    # Display Settings
    show_contact_section = models.BooleanField(default=True)

    show_projects_section = models.BooleanField(default=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Website Settings"
        verbose_name_plural = "Website Settings"

    def __str__(self):
        return self.site_name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
