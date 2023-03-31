import os
import re
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

import django

django.setup()


import random

from faker import Faker
from first_app.models import AccessRecord, Topic, Webpage

fakegen = Faker()

topics = ["Search", "Social", "Marketplace", "News", "Games"]


def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):

    for entry in range(N):
        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpage = Webpage.objects.get_or_create(
            topic=top, url=fake_url, name=fake_name
        )[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]


if __name__ == "__main__":
    print("populating scripts")
    populate(20)
    print("populating complete")
