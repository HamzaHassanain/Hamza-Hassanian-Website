from django.contrib import admin

# Register your models here.
from .models import ExperienceCategory, Experience

class ExperienceInline(admin.StackedInline):
    model = Experience
    extra = 1



class ExperienceCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    inlines = [ExperienceInline]


admin.site.register(ExperienceCategory, ExperienceCategoryAdmin)
