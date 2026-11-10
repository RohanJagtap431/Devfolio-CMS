
from django.contrib import admin
from .models import Experience


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):

    list_display = (
        "job_title",
        "company_name",
        "experience_type",
        "start_date",
        "end_date",
        "is_current",
    )

    list_filter = (
        "experience_type",
        "is_current",
    )

    search_fields = (
        "job_title",
        "company_name",
        "location",
    )

    list_editable = (
        "is_current",
    )

    readonly_fields = (
        "created_at",
    )

    fieldsets = (
        ("Experience Information", {
            "fields": (
                "job_title",
                "company_name",
                "experience_type",
                "location",
                "description",
            )
        }),

        ("Duration", {
            "fields": (
                "start_date",
                "end_date",
                "is_current",
            )
        }),

        ("Additional Information", {
            "fields": (
                "company_website",
                "display_order",
                "created_at",
            )
        }),
    )
