from django.contrib import admin

# Register your models here.



from .models import Contact
admin . site . register (Contact)

from .models import image
admin . site . register (image)

from .models import imageuploader
admin . site . register (imageuploader)