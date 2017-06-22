from django.contrib import admin
<<<<<<< HEAD

from .models import Post

class PostAdmin(admin.ModelAdmin):
    pass

=======
from .models import Post


# Post에 대한 ModelAdmin을 만들고 register
# 이후 /admin에 가서 Post확인하고 사진 첨부
class PostAdmin(admin.ModelAdmin):
    pass


>>>>>>> e5278c3fc0369ff8fa911dace01b1d0a28cb1c8d
admin.site.register(Post, PostAdmin)
