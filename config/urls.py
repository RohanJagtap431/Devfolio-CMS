
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap

from core.views import home, robots_txt
from contact.views import contact_submit

from projects.sitemaps import (
    StaticViewSitemap,
    ProjectSitemap,
)


sitemaps = {
    "static": StaticViewSitemap,
    "projects": ProjectSitemap,
}


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", home, name="home"),

    path(
        "contact/submit/",
        contact_submit,
        name="contact_submit"
    ),

    path("projects/", include("projects.urls")),

    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap"
    ),
    
    path("robots.txt", robots_txt, name="robots_txt"),
]
