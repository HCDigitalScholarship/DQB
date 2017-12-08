from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export import fields
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from import_export.widgets import ManyToManyWidget
from dqb_app.models import Person
from django.forms import *
from django.db import models
# Register your models here.
admin.site.register(Person)

