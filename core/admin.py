
from django.contrib import admin
from .models import SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Website Information", {
            "fields": (
                "site_name",
                "tagline",
                "footer_text",
            )
        }),

        ("SEO Settings", {
            "fields": (
                "meta_title",
                "meta_description",
                "meta_keywords",
            )
        }),

        ("Website Images", {
            "fields": (
                "favicon",
                "og_image",
            )
        }),

        ("Display Settings", {
            "fields": (
                "show_contact_section",
                "show_projects_section",
            )
        }),

        ("Metadata", {
            "fields": (
                "updated_at",
            )
        }),
    )

    readonly_fields = ("updated_at",)

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
