from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['titulo','cuerpo','imagen']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['cuerpo']
		widgets={
			'cuerpo': forms.Textarea(attrs={'class':'materialize-textarea'})
		}
		labels={
			'cuerpo':'Ecribe un comentario:'
		}