import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjectTwo.settings')

import django
django.setup()

from AppTwo import models
from faker import Faker

fakegen = Faker()


def populate(n=5):
    for entry in range(n):
        fake_name = fakegen.name().split()[-2:]
        fake_f_name,fake_l_name = fake_name
        fake_email = fakegen.email()
        user = models.User.objects.get_or_create(first_name=fake_f_name, last_name=fake_l_name,email=fake_email)

if __name__ == '__main__':
    populate(20)
