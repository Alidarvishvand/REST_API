from django.contrib import admin
from .models import person, question , answer
# Register your models here.
admin.site.register(person)
admin.site.register(question)
admin.site.register(answer)
