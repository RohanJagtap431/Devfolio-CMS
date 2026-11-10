
from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "subject",
        "is_read",
        "is_replied",
        "created_at",
    )

    list_filter = (
        "is_read",
        "is_replied",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "subject",
        "message",
    )

    readonly_fields = (
        "name",
        "email",
        "subject",
        "message",
        "created_at",
    )

    list_editable = (
        "is_read",
        "is_replied",
    )

    ordering = ("-created_at",)

    list_per_page = 20

    fieldsets = (
        ("Sender Information", {
            "fields": (
                "name",
                "email",
                "subject",
            )
        }),

        ("Message", {
            "fields": (
                "message",
            )
        }),

        ("Message Status", {
            "fields": (
                "is_read",
                "is_replied",
                "created_at",
            )
        }),
    )
    
    def has_add_permission(self, request):
        return False
