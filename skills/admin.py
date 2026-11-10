
from django.contrib import admin
from .models import Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "proficiency",
        "is_featured",
        "display_order",
    )

    list_filter = (
        "category",
        "is_featured",
    )

    search_fields = (
        "name",
    )

    list_editable = (
        "proficiency",
        "is_featured",
        "display_order",
    )

    ordering = (
        "display_order",
        "name",
    )
