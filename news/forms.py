from django import forms
from news.models import Category, New

class NewsFilterForm(forms.Form):
    search = forms.CharField(
        required=False,
        label='Sarlavha yoki matn',
        widget=forms.TextInput(attrs={'placeholder': 'Sarlavha yoki matn...', 'class': 'form-control'})
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label="Barcha kategoriyalar",
        widget=forms.Select(attrs={'class': 'form-select'})
    )



class AddNewsForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ['title', 'image', 'content', 'category']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
