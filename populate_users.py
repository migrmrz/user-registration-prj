import os
import django
from faker import Faker
from user_registration_app.models import User
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'user_registration_prj.settings'
)

django.setup()


fakegen = Faker()


def populate(N=5):
    for user in range(N):
        fake_full_name = fakegen.name().split()
        fake_first_name = fake_full_name[0]
        fake_last_name = fake_full_name[1]
        fake_user_mail = fakegen.email()

        # Create entry
        user = User.objects.get_or_create(
            first_name=fake_first_name,
            last_name=fake_last_name,
            user_mail=fake_user_mail)


if __name__ == "__main__":
    print("Populating datase. Please wait...")
    populate(20)
    print("Population complete!")
