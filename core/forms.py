from django import forms
from django.contrib.auth.models import User
from core.models import Profile
from books.models import Book


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture']

    def clean_picture(self):
        picture = self.cleaned_data['picture']
        if picture:
            return picture


class UserForm(forms.ModelForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.CharField(required=False)
    username = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_email(self):
        email = self.cleaned_data['email']
        if email:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("A user with this email already exists.")
            return email
        else:
            return None

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'image', 'quantity']
