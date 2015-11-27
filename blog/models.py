
#define the blog post

from django.db import models
from django.utils import timezone

LIT_TYPE = (  
    ('PM', 'poem'),
    ('SS', 'short story'),
    ('ES', 'essay'),
    ('DR', 'drama'),
)
#models.Model meant thathe Post is a Django model so it knows to save it
class Post(models.Model):
	author=models.ForeignKey('auth.User')
	title=models.CharField(max_length=200)
	literature_type=models.CharField(max_length=2, choices=LIT_TYPE)
	text=models.TextField()
	created_date=models.DateTimeField(
		 default=timezone.now)
	published_date=models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def __str__(self):
		return self.title

