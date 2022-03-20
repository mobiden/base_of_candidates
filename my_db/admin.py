from django.contrib import admin
from .models import Person, Company, Project, Projects_people

admin.site.register(Person)
admin.site.register(Company)
admin.site.register(Project)
admin.site.register(Projects_people)
