import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "s11luffycity.settings")
    import django
    django.setup()

from api import models




