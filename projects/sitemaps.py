
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Project


class StaticViewSitemap(Sitemap):

    priority = 1.0
    changefreq = "weekly"

    def items(self):
        return ["home"]

    def location(self, item):
        return reverse(item)


class ProjectSitemap(Sitemap):

    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Project.objects.all()

    def location(self, obj):
        return reverse(
            "project_detail",
            kwargs={"slug": obj.slug}
        )

    def lastmod(self, obj):
        return obj.updated_at
