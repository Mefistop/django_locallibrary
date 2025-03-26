import os
from django.contrib.auth import get_user_model

def create_superuser():
    """Create superuser, if it is not exist"""
    User = get_user_model()
    username = os.getenv('DJANGO_SUPERUSER_USERNAME')
    password = os.getenv('DJANGO_SUPERUSER_PASSWORD')
    email = os.getenv('DJANGO_SUPERUSER_EMAIL', '')

    if not User.objects.filter(username=username).exists():
        print('Create superuser....')
        User.objects.create_superuser(username=username, password=password, email=email)
        print('Superuser created successfully.')
    else:
        print('Superuser already exists.')


if __name__ == '__main__':
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'locallibrary.settings')
    django.setup()
    create_superuser()