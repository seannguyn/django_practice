import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','second_project.settings')

import django
django.setup()

from faker import Faker
import random
from second_app.models import User

fakegen = Faker()

def populate_data(N=5):
    for entry in range(N):
        fake_name = fakegen.name()
        fake_email = fakegen.email()
        fake_password = fakegen.password()

        user = User.objects.get_or_create(name=fake_name,email=fake_email,password=fake_password)


if __name__ == "__main__":
    populate_data(10)
    print("populated")
