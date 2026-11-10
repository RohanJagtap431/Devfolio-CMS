
from django.db import models


class Experience(models.Model):

    EXPERIENCE_TYPES = [
        ("internship", "Internship"),
        ("job", "Full-time Job"),
        ("part_time", "Part-time Job"),
        ("freelance", "Freelance"),
        ("volunteer", "Volunteering"),
    ]

    job_title = models.CharField(max_length=150)

    company_name = models.CharField(max_length=150)

    experience_type = models.CharField(
        max_length=20,
        choices=EXPERIENCE_TYPES
    )

    location = models.CharField(max_length=150, blank=True)

    description = models.TextField()

    start_date = models.DateField()

    end_date = models.DateField(
        blank=True,
        null=True
    )

    is_current = models.BooleanField(default=False)

    company_website = models.URLField(blank=True)

    display_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-start_date", "display_order"]
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"

    def __str__(self):
        return f"{self.job_title} - {self.company_name}"
