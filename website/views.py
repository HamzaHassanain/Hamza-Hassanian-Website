from django.shortcuts import render
from hero.models import Hero, BladeIcon
from metatags.models import MetaTags
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
        "image_url": hero_object.image.url,
        "resume_url": hero_object.resume_url,
    }
    # update image url to have https
    hero['image_url'] = hero['image_url'].replace('http://', 'https://')
    return hero

def load_meta_tags():
    if MetaTags.objects.count() == 0:
        created_meta_tags = MetaTags()
        created_meta_tags.save()

    meta_tags_object = MetaTags.objects.all()[0]
    
    meta_tags = {
        "title": meta_tags_object.title,
        "description": meta_tags_object.description,
        "keywords": meta_tags_object.keywords,
        "author": meta_tags_object.author,
        "image_url": meta_tags_object.image.url,
        "url": meta_tags_object.url,
        "site_name": meta_tags_object.site_name,
        "type": meta_tags_object.type,
        "twitter_creator": meta_tags_object.twitter_creator,
    }
    # update image url to have https
    meta_tags['image_url'] = meta_tags['image_url'].replace('http://', 'https://')

    return meta_tags
def load_links():
    links = []
    blade_icons_objects = BladeIcon.objects.all()
    for blade_icon in blade_icons_objects:
        link = {
            "name": blade_icon.name,
            "link": blade_icon.link,
            "blade_icon_code": blade_icon.blade_icon_code,
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
        experience_objects = Experience.objects.filter(category_id=experience_category.id).order_by('priority')
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
            "thumbnail_url": personal_project_object.thumbnail.url,
        }
        # update thumbnail url to have https
        personal_project['thumbnail_url'] = personal_project['thumbnail_url'].replace('http://', 'https://')
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
        "metatags": load_meta_tags(),
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
        "thumbnail_url": personal_project.thumbnail.url,
    }
    # update thumbnail url to have https
    parsed_project['thumbnail_url'] = parsed_project['thumbnail_url'].replace('http://', 'https://')
    context = {
        "title": "Hamza - " + parsed_project['name'],
        "links": load_links(),
        "metatags": load_meta_tags(),
        "project": parsed_project,
    }
    print(context['links'])
    return render(request, "works-setails.html" , context)