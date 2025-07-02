from django.contrib import admin
from jobs.models import *

# Register your models here.
admin.site.register(Job)
admin.site.register(JobCategory)
admin.site.register(Company)