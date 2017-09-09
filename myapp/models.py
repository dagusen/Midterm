from django.db import models

from django.utils import timezone

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	detail = models.ManyToManyField ("Detail",related_name="Post")
	
	def publish(self):
		self.published_date = timezone.now()

	def __str__(self):
		return "{} by {}".format(self.title,self.list_detail())
		#return self.first_name

	def list_detail(self):
		return ",".join([detail.first_name for detail in self.detail.all()])

	def save(self, *args, **kwargs):
		super(Post, self).save(*args, **kwargs)

class Detail(models.Model):
	first_name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150)
	middle_name = models.CharField(max_length=150)
	age = models.IntegerField()
	
	def __str__(self):
		return self.first_name

