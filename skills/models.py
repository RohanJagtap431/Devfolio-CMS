
from django.db import models


class Skill(models.Model):

    CATEGORY_CHOICES = [
        ("programming", "Programming Languages"),
        ("backend", "Backend Development"),
        ("database", "Database"),
        ("frontend", "Frontend Development"),
        ("tools", "Tools & Technologies"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=100)

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    proficiency = models.PositiveSmallIntegerField(
        default=50,
        help_text="Skill level from 0 to 100"
    )

    is_featured = models.BooleanField(default=True)

    display_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["display_order", "name"]
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return f"{self.name} - {self.get_category_display()}"
