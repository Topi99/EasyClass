from django.contrib.auth.models import User
from .models import Profile

class EmailAuthBackend(object):
	"""	
	Autentica al usuario con su Email
	"""
	def authenticate(self, username=None, password=None):
		try:
			user = User.objects.get(email=username)
			if user.check_password(password):
				return user
			return None			
		except User.DoesNotExist:
			return None

	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except:
			return None

class TelAuthBackend(object):
	"""
	Autentica al usario con su Telefono
	"""
	def authenticate(self, username=None, password=None):
		try:
			perfil = Profile.objects.get(tel=username)
			user = perfil.user
			if user.check_password(password):
				return user
			return None
		except User.DoesNotExist:
			return None
	
	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except:
			return None