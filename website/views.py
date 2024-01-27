from django.shortcuts import render
from hero.models import Hero, BladeIcon
from skills.models import SkillsCategory, Skill
# Create your views here.
def index(request):
    if Hero.objects.count() == 0:
        created_hero = Hero(slug="hamza-hassanain", small_title="Hamza Hassanain", big_title="Software Engineer")
        created_hero.save()



    hero_object = Hero.objects.all()[0]
    blade_icons_objects = BladeIcon.objects.all()
    links = []
    skills = []
    hero = {
        "slug": hero_object.slug,
        "small_title": hero_object.small_title,
        "big_title": hero_object.big_title,
        "about_me": hero_object.about_me,
        "image": hero_object.image,
        "resume_url": hero_object.resume_url,
    }
    for blade_icon in blade_icons_objects:
        link = {
            "name": blade_icon.name,
            "link": blade_icon.link,
            "blade_icon_code": blade_icon.blad_icon_code,
        }
        links.append(link)

    skills_categories = SkillsCategory.objects.all()
    for skills_category in skills_categories:
        skill_items = []
        skills_objects = Skill.objects.filter(category_id=skills_category.id)
        for skill in skills_objects:
            skill_object = {
                "name": skill.name,
            }
            skill_items.append(skill_object)
        skills_category = {
            "name": skills_category.name,
            "skill_items": skill_items,
        }
        skills.append(skills_category)
    context = {
        "title": "Hamza - Home",
        "links": links,
        "hero": hero,
        "skills": skills,
    }
    return render(request, "index.html" , context)