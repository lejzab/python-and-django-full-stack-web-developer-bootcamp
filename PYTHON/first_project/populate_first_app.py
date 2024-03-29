import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
from first_app.models import Webpage,AccessRecord,Topic
from faker import Faker

fakegen = Faker()

topics = ('Search', 'Games', 'Social', 'Marketplace', 'News')

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    # t.save()
    return t

def populate(n=5):
    for entry in range(n):
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpage = Webpage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]

        access_recored = AccessRecord.objects.get_or_create(name=webpage,date=fake_date)[0]

if __name__ == '__main__':
    populate(20)
