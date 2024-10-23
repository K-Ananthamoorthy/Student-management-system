from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Create a superuser with a specified user type'

    def handle(self, *args, **options):
        User = get_user_model()
        username = input("Enter username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        user_type = input("Enter user type (1 for Student, 2 for Teacher, 3 for Admin): ")

        try:
            user = User.objects.create_superuser(username=username, email=email, password=password, user_type=int(user_type))
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully!'))
        except IntegrityError:
            self.stdout.write(self.style.ERROR(f'User "{username}" already exists.'))
        except ValueError:
            self.stdout.write(self.style.ERROR('Invalid user type. Please enter 1, 2, or 3.'))