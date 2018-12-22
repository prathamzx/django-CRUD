from django.forms import ModelForm
from .models import Post

class NameForm(ModelForm):
    class Meta:
        model=Post
        fields=["username"]

class Form(ModelForm):
    class Meta:
        model=Post
        fields="__all__"

class DeleteNewForm(ModelForm):
    class Meta:
        model = Post
        fields = []
