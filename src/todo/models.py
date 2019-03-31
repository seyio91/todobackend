from django.db import models

# Create your models here.


#creating our models
class TodoItems(models.Model):
	title = models.CharField(max_length=256, null=True, blank=True)
	completed = models.BooleanField(blank=True, default=False)
	url = models.CharField(max_length=256, null=True, blank=True)
	order = models.IntegerField(null=True, blank=True)