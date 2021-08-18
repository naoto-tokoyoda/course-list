import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()

from app.models import Course
from faker import Faker

faker = Faker()

def populate(n=5):
	for entry in range(n):
		fake_name = faker.name().split()
		fake_first_name = fake_name[0]
		fake_last_name = fake_name[1]
		fake_email = faker.email()

		user = User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)


if __name__ == '__main__':
	print("Populating database")
	populate(30)
	print("complete.")
else:
	print("Something went wrong")

