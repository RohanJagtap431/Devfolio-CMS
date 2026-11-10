
from django.contrib import admin
from .models import Certificate


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "issuing_organization",
        "issue_date",
        "expiry_date",
        "is_featured",
    )

    list_filter = (
        "issuing_organization",
        "is_featured",
    )

    search_fields = (
        "title",
        "issuing_organization",
        "credential_id",
    )

    list_editable = (
        "is_featured",
    )

    readonly_fields = (
        "created_at",
    )

    fieldsets = (
        ("Certificate Information", {
            "fields": (
                "title",
                "issuing_organization",
                "description",
            )
        }),

        ("Certificate Details", {
            "fields": (
                "issue_date",
                "expiry_date",
                "credential_id",
                "credential_url",
                "certificate_file",
            )
        }),

        ("Display Settings", {
            "fields": (
                "is_featured",
                "display_order",
                "created_at",
            )
        }),
    )
