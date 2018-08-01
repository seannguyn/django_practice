# 2 default line

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

from faker import Faker

import random

from first_app.models import Topic, WebPage, AccessRecors

fakegen = Faker()

topics = ['Social','Webpage','News']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):

        top = add_topic()

        fake_name = fakegen.company()
        fake_url = fakegen.url()
        fake_data = fakegen.date()

        webpg = WebPage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]

        records = AccessRecors.objects.get_or_create(name=webpg,date=fake_data)[0]

if __name__ == '__main__':
    print("populating script")
    populate(20)
    print("populating complete")
