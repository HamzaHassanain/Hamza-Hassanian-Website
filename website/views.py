from django.shortcuts import render
from hero.models import Hero, BladeIcon
from skills.models import SkillsCategory, Skill
from experience.models import ExperienceCategory, Experience
from personal_projects.models import PersonalProject
# Create your views here.

def load_hero():
    if Hero.objects.count() == 0:
        created_hero = Hero(slug="hamza-hassanain", small_title="Hamza Hassanain", big_title="Software Engineer")
        created_hero.save()

    hero_object = Hero.objects.all()[0]
    hero = {
        "slug": hero_object.slug,
        "small_title": hero_object.small_title,
        "big_title": hero_object.big_title,
        "about_me": hero_object.about_me,
        "image": hero_object.image,
        "resume_url": hero_object.resume_url,
    }

    return hero
def load_links():
    links = []
    blade_icons_objects = BladeIcon.objects.all()
    for blade_icon in blade_icons_objects:
        link = {
            "name": blade_icon.name,
            "link": blade_icon.link,
            "blade_icon_code": blade_icon.icon_code,
        }
        links.append(link)
    return links
def load_skills():
    skills = []
    skills_categories = SkillsCategory.objects.all().order_by('priority')
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
    return skills

def load_experience():
    experiences = []
    experience_categories = ExperienceCategory.objects.all().order_by('priority')
    for experience_category in experience_categories:
        experience_items = []
        experience_objects = Experience.objects.filter(category_id=experience_category.id)
        for experience_object in experience_objects:
            experience_item = {
                "name": experience_object.name,
                "title": experience_object.title,
                "subtitle": experience_object.subtitle,
                "description": experience_object.description,
                "start_date": experience_object.start_date,
                "end_date": experience_object.end_date,
            }
            experience_items.append(experience_item)
        experience_category = {
            "name": experience_category.name,
            "experience_items": experience_items,
        }
        experiences.append(experience_category)
    return experiences

def load_personal_projects():
    personal_projects = []
    personal_projects_objects = PersonalProject.objects.all().order_by('priority')
    for personal_project_object in personal_projects_objects:
        personal_project = {
            "name": personal_project_object.name,
            "title": personal_project_object.title,
            "slug": personal_project_object.slug,
            "small_description": personal_project_object.small_description,
            "description": personal_project_object.description,
            "thumbnail": personal_project_object.thumbnail,
        }
        personal_projects.append(personal_project)
    return personal_projects

def index(request):
   
    context = {
        "title": "Hamza - Home",
        "links": load_links(),
        "hero": load_hero(),
        "skills": load_skills(),
        "experiences": load_experience(),
        "personal_projects": load_personal_projects(),
    }
    return render(request, "index.html" , context)


def single_project(request, slug):
    personal_project = PersonalProject.objects.get(slug=slug)
    parsed_project = {
        "name": personal_project.name,
        "title": personal_project.title,
        "slug": personal_project.slug,
        "small_description": personal_project.small_description,
        "description": personal_project.description,
        "thumbnail": personal_project.thumbnail,
    }
    context = {
        "title": "Hamza - " + parsed_project['name'],
        "links": load_links(),
        "project": parsed_project,
    }
    print(context['links'])
    return render(request, "works-setails.html" , context)