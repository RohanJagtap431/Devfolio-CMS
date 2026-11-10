
from django.shortcuts import render

from portfolio.models import PortfolioProfile
from skills.models import Skill
from projects.models import Project
from experience.models import Experience
from certificates.models import Certificate
from core.models import SiteSettings


def home(request):

    profile = PortfolioProfile.objects.first()
    settings = SiteSettings.objects.first()

    skills = Skill.objects.all()

    # Get all projects
    projects = Project.objects.all().order_by(
        "display_order",
        "-created_at"
    )

    featured_projects = projects.filter(
        is_featured=True
    )

    experiences = Experience.objects.all()

    certificates = Certificate.objects.all()

    context = {
        "profile": profile,
        "site_settings": settings,
        "skills": skills,
        "projects": projects,
        "featured_projects": featured_projects,
        "experiences": experiences,
        "certificates": certificates,
    }

    return render(
        request,
        "core/home.html",
        context
    )


from django.http import HttpResponse


def robots_txt(request):
    content = """User-agent: *
Allow: /

Disallow: /admin/
Disallow: /contact/submit/

Sitemap: https://YOUR-DOMAIN.com/sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain")