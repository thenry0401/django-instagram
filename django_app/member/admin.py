from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from django.contrib.auth.admin import UserAdmin

from .models import User

admin.site.register(User, UserAdmin)
>>>>>>> e5278c3fc0369ff8fa911dace01b1d0a28cb1c8d
