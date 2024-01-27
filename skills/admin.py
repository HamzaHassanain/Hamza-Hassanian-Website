from django.contrib import admin

# Register your models here.

from .models import SkillsCategory, Skill

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


class SkillsCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    inlines = [SkillInline]


admin.site.register(SkillsCategory, SkillsCategoryAdmin)

