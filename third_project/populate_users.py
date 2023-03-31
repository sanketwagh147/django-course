import os
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "third_project.settings")

import django

django.setup()


from faker import Faker
from third_app.models import User

fakegen = Faker()


def populate(N=5):

    for entry in range(N):
        name = fakegen.name().split(" ")
        fake_first = name[0]
        fake_last = name[1]
        fake_email = fakegen.email()

        t = User.objects.get_or_create(
            first_name=fake_first, last_name=fake_last, email=fake_email
        )[0]
        t.save()


if __name__ == "__main__":
    print("populating scripts")
    populate(20)
    print("populating complete")
