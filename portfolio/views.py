from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .models import (
    Profile,
    SocialLink,
    Education,
    Skill,
    Service,
    Project,
    Experience,
    Achievement,
    BlogPost,
    Testimonial,
    ContactMessage,
)


def home(request):

    profile = Profile.objects.first()

    social_links = SocialLink.objects.filter(
        is_active=True
    )

    education = Education.objects.all()

    skills = Skill.objects.all()

    services = Service.objects.filter(
        is_active=True
    )

    projects = Project.objects.filter(
        featured=True
    )[:6]

    experiences = Experience.objects.all()

    achievements = Achievement.objects.all()[:6]

    testimonials = Testimonial.objects.filter(
        is_active=True
    )

    blog_posts = BlogPost.objects.filter(
        published=True
    )[:3]

    context = {
        "profile": profile,

        "social_links": social_links,

        "education": education,

        "skills": skills,

        "services": services,

        "projects": projects,

        "experiences": experiences,

        "achievements": achievements,

        "testimonials": testimonials,

        "blog_posts": blog_posts,
    }

    return render(
        request,
        "portfolio/home.html",
        context
    )


def project_detail(request, slug):

    project = get_object_or_404(
        Project,
        slug=slug
    )

    return render(
        request,
        "portfolio/project_detail.html",
        {
            "project": project
        }
    )


def blog_detail(request, slug):

    post = get_object_or_404(
        BlogPost,
        slug=slug,
        published=True
    )

    return render(
        request,
        "portfolio/blog_detail.html",
        {
            "post": post
        }
    )


def contact(request):

    if request.method == "POST":

        name = request.POST.get("name", "").strip()

        email = request.POST.get("email", "").strip()

        subject = request.POST.get("subject", "").strip()

        message = request.POST.get("message", "").strip()

        if name and email and subject and message:

            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )

            messages.success(
                request,
                "Your message has been sent successfully."
            )

        else:

            messages.error(
                request,
                "Please fill in all fields."
            )

    return redirect(
        "portfolio:home"
    )