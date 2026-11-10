
from django.contrib import admin
from .models import PortfolioProfile


@admin.register(PortfolioProfile)
class PortfolioProfileAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "professional_title",
        "email",
        "is_available_for_work",
        "updated_at",
    )

    search_fields = (
        "full_name",
        "email",
        "professional_title",
    )

    list_filter = (
        "is_available_for_work",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        ("Personal Information", {
            "fields": (
                "full_name",
                "professional_title",
                "profile_photo",
                "short_bio",
                "about_me",
            )
        }),

        ("Contact Information", {
            "fields": (
                "email",
                "phone",
                "location",
            )
        }),

        ("Social Media", {
            "fields": (
                "github_url",
                "linkedin_url",
                "instagram_url",
            )
        }),

        ("Resume & Availability", {
            "fields": (
                "resume",
                "is_available_for_work",
            )
        }),

        ("Timestamps", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )
