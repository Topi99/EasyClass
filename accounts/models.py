from django.db import models
from django.conf import settings

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	date_of_birth = models.DateField(blank=True, null=True)
	foto = models.ImageField(upload_to="users/%Y/%m/%d", blank=True)
	avatar = models.ImageField(upload_to="users/%Y/%m/%d", blank=True, null=True)
	bio = models.TextField(blank=True, null=True)
	tel = models.IntegerField(default=000, blank=True, null=True) 

	def __str__(self):
		return 'Perfil del usuario {}'.format(self.user.username)