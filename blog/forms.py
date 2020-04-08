from django import forms
from blog.models import Post,Comments

class postForm(forms.ModelForm):
    class Meta():
        model= Post
        fields=('author','title','text') #mention editable fields

        widgets={
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
            #editable , medium-editor-textarea are default classes
        }

class commentForm(forms.ModelForm):
    class Meta():
        model = Comments
        fields = ('author','text')

        widgets={
            'author': forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea '})
            #editable , medium-editor-textarea are default classes
        }


