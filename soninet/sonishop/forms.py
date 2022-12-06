from django import forms
from .models import Photo, Article

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['author', 'photo'] 

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'author-photo', 'type':'hidden'}),
        }
        photo = forms.ImageField()
        help_texts = {
            'photo': 'Vous pouvez ajouter jusqu\'à 3 photos à votre annonce',
        }
        labels={'author' : "auteur", 'photo': 'photo'}


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['author', 'title', 'details', 'price'] 

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'id':'author-article', 'type':'hidden'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'id':'title', 'placeholder': 'Ajouter un titre à votre annonce'}),
            'details': forms.Textarea(attrs={'class': 'form-control', 'id':'details', 'placeholder': 'Détailler votre annonce'}),
        }
        price = forms.FloatField(),
        help_texts = {
            'price': 'ajouter un prix. Si c\'est un decimal séparer par un point',
        }
        labels={'price' : "prix"}