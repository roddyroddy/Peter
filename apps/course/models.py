from __future__ import unicode_literals
from django.db import models
import re

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
