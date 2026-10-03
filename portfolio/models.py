from django.db import models
from django.urls import reverse


# ==================================================
# PROFILE
# ==================================================

class Profile(models.Model):

    name = models.CharField(
        max_length=100
    )

    title = models.CharField(
        max_length=200,
        default="Computer Science & Engineering Student"
    )

    short_bio = models.TextField(
        max_length=500
    )

    about = models.TextField()

    profile_image = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True
    )

    cv = models.FileField(
        upload_to="cv/",
        blank=True,
        null=True
    )

    email = models.EmailField(
        blank=True
    )

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    location = models.CharField(
        max_length=200,
        blank=True
    )

    available_for_work = models.BooleanField(
        default=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.name


# ==================================================
# SOCIAL LINKS
# ==================================================

class SocialLink(models.Model):

    PLATFORM_CHOICES = [

        ("github", "GitHub"),

        ("linkedin", "LinkedIn"),

        ("facebook", "Facebook"),

        ("instagram", "Instagram"),

        ("youtube", "YouTube"),

        ("twitter", "Twitter"),

    ]

    platform = models.CharField(
        max_length=30,
        choices=PLATFORM_CHOICES
    )

    url = models.URLField()

    icon = models.CharField(
        max_length=50,
        default="fa-link"
    )

    order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.get_platform_display()


# ==================================================
# EDUCATION
# ==================================================

class Education(models.Model):

    degree = models.CharField(
        max_length=200
    )

    institution = models.CharField(
        max_length=200
    )

    location = models.CharField(
        max_length=200,
        blank=True
    )

    start_year = models.PositiveIntegerField()

    end_year = models.CharField(
        max_length=20,
        help_text="Example: 2028 or Present"
    )

    description = models.TextField(
        blank=True
    )

    result = models.CharField(
        max_length=100,
        blank=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["-start_year", "order"]

    def __str__(self):
        return f"{self.degree} - {self.institution}"


# ==================================================
# SKILL
# ==================================================

class Skill(models.Model):

    name = models.CharField(
        max_length=100
    )

    percentage = models.PositiveIntegerField(
        default=70
    )

    category = models.CharField(
        max_length=100,
        default="Technical"
    )

    icon = models.CharField(
        max_length=50,
        default="fa-code"
    )

    order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name


# ==================================================
# SERVICE
# ==================================================

class Service(models.Model):

    title = models.CharField(
        max_length=150
    )

    description = models.TextField()

    icon = models.CharField(
        max_length=50,
        default="fa-code"
    )

    order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


# ==================================================
# PROJECT
# ==================================================

class Project(models.Model):

    title = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        unique=True
    )

    short_description = models.TextField(
        max_length=300
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to="projects/"
    )

    technologies = models.CharField(
        max_length=500,
        help_text="Separate technologies with commas."
    )

    github_url = models.URLField(
        blank=True
    )

    live_url = models.URLField(
        blank=True
    )

    featured = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "portfolio:project_detail",
            kwargs={"slug": self.slug}
        )

    def technology_list(self):
        return [
            technology.strip()
            for technology in self.technologies.split(",")
            if technology.strip()
        ]


# ==================================================
# EXPERIENCE
# ==================================================

class Experience(models.Model):

    position = models.CharField(
        max_length=200
    )

    company = models.CharField(
        max_length=200
    )

    start_date = models.DateField()

    end_date = models.DateField(
        blank=True,
        null=True
    )

    current = models.BooleanField(
        default=False
    )

    description = models.TextField()

    order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.position} - {self.company}"


# ==================================================
# ACHIEVEMENT
# ==================================================

class Achievement(models.Model):

    title = models.CharField(
        max_length=200
    )

    organization = models.CharField(
        max_length=200,
        blank=True
    )

    description = models.TextField()

    date = models.DateField(
        blank=True,
        null=True
    )

    certificate = models.FileField(
        upload_to="certificates/",
        blank=True,
        null=True
    )

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title


# ==================================================
# BLOG
# ==================================================

class BlogPost(models.Model):

    title = models.CharField(
        max_length=250
    )

    slug = models.SlugField(
        unique=True
    )

    excerpt = models.TextField(
        max_length=400
    )

    content = models.TextField()

    image = models.ImageField(
        upload_to="blog/",
        blank=True,
        null=True
    )

    published = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "portfolio:blog_detail",
            kwargs={"slug": self.slug}
        )


# ==================================================
# TESTIMONIAL
# ==================================================

class Testimonial(models.Model):

    name = models.CharField(
        max_length=100
    )

    role = models.CharField(
        max_length=150,
        blank=True
    )

    message = models.TextField()

    image = models.ImageField(
        upload_to="testimonials/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


# ==================================================
# CONTACT MESSAGE
# ==================================================

class ContactMessage(models.Model):

    name = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    subject = models.CharField(
        max_length=200
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_read = models.BooleanField(
        default=False
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.subject}"