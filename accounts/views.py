from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserRegistrationForm, ProfileEditForm, UserEditForm
from .models import Profile

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class Dashboard(View):
	@method_decorator(login_required)
	def get(self, request):
		if request.user.profile:
			template_name = "accounts/perfil.html"
			user_form = UserEditForm(instance=request.user)
			profile_form = ProfileEditForm(instance=request.user.profile)
			context = {
				'user_form':user_form,
				'profile_form':profile_form
			}
			return render(request, template_name, context)
		else:
			profile = Profile()
			profile.user = request.user.save(commit=False)
			profile.save()
			return redirect('profile')
			
	def post(self, request):
		template_name = "accounts/perfil.html"
		
		user_form = UserEditForm(data=request.POST, instance=request.user)
		profile_form = ProfileEditForm(data=request.POST, files=request.FILES, instance=request.user.profile)

		if user_form.is_valid() and profile_form.is_valid():
			user_info = user_form.save(commit=False)
			profile_info = profile_form.save(commit=False)
			user_info.save()
			profile_info.save()
			context = {
				'user_form':user_form,
				'profile_form':profile_form
			}
			return render(request, template_name, context)
		else:
			context = {}
			return render(request, template_name, context)

class Registration(View):
	def get(self, request):
		form = UserRegistrationForm()
		template_name = 'accounts/registration.html'
		context = {
			'form':form
		}
		return render(request, template_name, context)

	def post(self, request):
		new_user_form = UserRegistrationForm(request.POST)
		if new_user_form.is_valid():
			new_user = new_user_form.save(commit=False)
			new_user.set_password(new_user_form.cleaned_data['password'])
			new_user.save()

			perfil = Profile()
			perfil.user = new_user
			perfil.save()

			return redirect('perfil')
		else:
			template_name = 'accounts/registration.html'
			context = {
				'form':new_user_form(request.POST)
			}
			return render(request, template_name, context)

class CompleteProfile(View):
	def get(self, request):
		form = ProfileEditForm()
		template_name = 'accounts/complete-prof.html'
		context = {
			'form':form
		}
		return render(request, template_name,context)
	def post(self, request):
		user = request
		profile_form = ProfileEditForm(data=request.POST, files=request.FILES)
		if profile_form.is_valid():
			profile_form.save()
			return redirect('perfil')
		else:
			template_name = "accounts/complete-prof.html"
			context = {}
			return render(request, template_name, context)