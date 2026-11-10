
from django.db import models


class Project(models.Model):

    STATUS_CHOICES = [
        ("completed", "Completed"),
        ("in_progress", "In Progress"),
        ("planned", "Planned"),
    ]

    # Basic Information
    title = models.CharField(max_length=200)

    slug = models.SlugField(
        unique=True,
        max_length=220
    )

    short_description = models.CharField(
        max_length=300
    )

    description = models.TextField()

    # Project Image
    thumbnail = models.ImageField(
        upload_to="portfolio/projects/",
        blank=True,
        null=True
    )

    # Technologies
    technologies = models.CharField(
        max_length=500,
        help_text="Example: Python, Django, PostgreSQL, HTML, CSS"
    )

    # Project Links
    github_url = models.URLField(blank=True)
    live_demo_url = models.URLField(blank=True)

    # Project Settings
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="completed"
    )

    is_featured = models.BooleanField(default=False)

    display_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order", "-created_at"]
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title
    


class ProjectFeature(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="features"
    )

    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return f"{self.project.title} - {self.title}"


class ProjectChallenge(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="challenges"
    )

    challenge = models.TextField()

    solution = models.TextField()

    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return f"{self.project.title} - Challenge"


class ProjectImage(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="gallery"
    )

    image = models.ImageField(
        upload_to="portfolio/project-gallery/"
    )

    caption = models.CharField(
        max_length=200,
        blank=True
    )

    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return f"{self.project.title} - Gallery Image"

