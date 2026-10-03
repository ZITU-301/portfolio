from django.contrib import admin

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


# ==================================================
# PROFILE
# ==================================================

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "title",
        "email",
        "available_for_work",
        "updated_at",
    )

    list_filter = (
        "available_for_work",
    )

    search_fields = (
        "name",
        "title",
        "email",
    )


# ==================================================
# SOCIAL
# ==================================================

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):

    list_display = (
        "platform",
        "url",
        "order",
        "is_active",
    )

    list_filter = (
        "platform",
        "is_active",
    )

    list_editable = (
        "order",
        "is_active",
    )


# ==================================================
# EDUCATION
# ==================================================

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):

    list_display = (
        "degree",
        "institution",
        "start_year",
        "end_year",
        "order",
    )

    search_fields = (
        "degree",
        "institution",
    )

    list_editable = (
        "order",
    )


# ==================================================
# SKILL
# ==================================================

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "percentage",
        "order",
    )

    list_filter = (
        "category",
    )

    list_editable = (
        "percentage",
        "order",
    )

    search_fields = (
        "name",
    )


# ==================================================
# SERVICE
# ==================================================

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "order",
        "is_active",
    )

    list_editable = (
        "order",
        "is_active",
    )

    search_fields = (
        "title",
    )


# ==================================================
# PROJECT
# ==================================================

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "featured",
        "created_at",
    )

    list_filter = (
        "featured",
    )

    list_editable = (
        "featured",
    )

    search_fields = (
        "title",
        "technologies",
        "short_description",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }


# ==================================================
# EXPERIENCE
# ==================================================

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):

    list_display = (
        "position",
        "company",
        "start_date",
        "end_date",
        "current",
    )

    list_filter = (
        "current",
    )

    search_fields = (
        "position",
        "company",
    )


# ==================================================
# ACHIEVEMENT
# ==================================================

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "organization",
        "date",
    )

    search_fields = (
        "title",
        "organization",
    )


# ==================================================
# BLOG
# ==================================================

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "published",
        "created_at",
    )

    list_filter = (
        "published",
    )

    search_fields = (
        "title",
        "excerpt",
        "content",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }


# ==================================================
# TESTIMONIAL
# ==================================================

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "role",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "role",
    )


# ==================================================
# CONTACT
# ==================================================

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "subject",
        "created_at",
        "is_read",
    )

    list_filter = (
        "is_read",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "subject",
        "message",
    )

    list_editable = (
        "is_read",
    )

    readonly_fields = (
        "name",
        "email",
        "subject",
        "message",
        "created_at",
    )