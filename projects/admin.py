
from django.contrib import admin

from .models import (
    Project,
    ProjectFeature,
    ProjectChallenge,
    ProjectImage,
)


class ProjectFeatureInline(admin.TabularInline):
    model = ProjectFeature
    extra = 1


class ProjectChallengeInline(admin.TabularInline):
    model = ProjectChallenge
    extra = 1


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "status",
        "is_featured",
        "display_order",
        "created_at",
    )

    list_filter = (
        "status",
        "is_featured",
    )

    search_fields = (
        "title",
        "short_description",
        "technologies",
    )

    list_editable = (
        "status",
        "is_featured",
        "display_order",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    inlines = [
        ProjectFeatureInline,
        ProjectChallengeInline,
        ProjectImageInline,
    ]

    fieldsets = (
        ("Project Information", {
            "fields": (
                "title",
                "slug",
                "short_description",
                "description",
                "thumbnail",
            )
        }),

        ("Technologies", {
            "fields": ("technologies",)
        }),

        ("Project Links", {
            "fields": (
                "github_url",
                "live_demo_url",
            )
        }),

        ("Project Settings", {
            "fields": (
                "status",
                "is_featured",
                "display_order",
            )
        }),

        ("Timestamps", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )
