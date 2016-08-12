from django.shortcuts import reverse
from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

class Post(models.Model):
	""" 
	ESte modelo usa Tags
	"""
	tags = TaggableManager()
	titulo = models.CharField(max_length=140)
	cuerpo = models.TextField()
	fecha = models.DateTimeField(auto_now=True)	
	publicado = models.BooleanField(default=False)
	autor = models.ForeignKey(User, related_name='publicaciones')
	imagen = models.ImageField(upload_to="assets")
	slug = models.SlugField(max_length=280)

	class Meta:
		ordering = ('-fecha',)

	def get_absolute_url(self):
		return reverse('posts:detail', args=[self.slug])

	def __str__(self):
		return self.titulo

class Comment(models.Model):
	autor = models.ForeignKey(User, related_name='comentarios')
	post = models.ForeignKey(Post, related_name='comentarios')
	fecha = models.DateTimeField(auto_now=True)
	cuerpo = models.TextField()

	def __str__(self):
		return '{} comento en {}'.format(self.autor, self.post)

	class Meta:
		ordering = ('-fecha',)