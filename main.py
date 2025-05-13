import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "user_rosclad.settings")

django.setup()

from user.models import Subject 
from datetime import datetime

name = input("Назва предмету: ")
description = input("Опис: ")

if Subject.objects.filter(name=name).exists():
    print("Такий предмет вже існує.")
else:
    Subject.objects.create(name=name, description=description)
    print("Предмет додано.")