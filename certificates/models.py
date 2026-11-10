
from django.db import models


class Certificate(models.Model):

    title = models.CharField(max_length=200)

    issuing_organization = models.CharField(
        max_length=150
    )

    description = models.TextField(blank=True)

    issue_date = models.DateField()

    expiry_date = models.DateField(
        blank=True,
        null=True
    )

    credential_id = models.CharField(
        max_length=150,
        blank=True
    )

    credential_url = models.URLField(blank=True)

    certificate_file = models.FileField(
        upload_to="portfolio/certificates/",
        blank=True,
        null=True
    )

    is_featured = models.BooleanField(default=True)

    display_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-issue_date", "display_order"]
        verbose_name = "Certificate"
        verbose_name_plural = "Certificates"

    def __str__(self):
        return self.title
