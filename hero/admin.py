from django.contrib import admin
from .models import Hero, BladeIcon
# Register your models here.
class InlineBladeIcon(admin.TabularInline):
    model = BladeIcon
    extra = 1

class HeroAdmin(admin.ModelAdmin):
    list_display = ("slug", "small_title", "big_title")
    inlines = [InlineBladeIcon]

# change admin site title
admin.site.site_header = "Hamza Hassanain"
admin.site.site_title = "Hamza Hassanain"
admin.site.index_title = "Welcome to Hamza Hassanain's Dashboard"


admin.site.register(Hero, HeroAdmin)
