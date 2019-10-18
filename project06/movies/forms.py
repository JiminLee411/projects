from django import forms
from .models import Movie, Review

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        max_length=455,
        label='제목',
        widget=forms.TextInput(
            attrs={
                'placeholder': '제목(국문)을 입력하세요.'
            }
        )
            )
    title_en = forms.CharField(
        max_length=455,
        label='제목',
        widget=forms.TextInput(
            attrs={
                'placeholder': '제목(영문)을 입력하세요.'
            }
        )
            )
    description = forms.CharField(
        max_length=455,
        label='줄거리',
        widget=forms.Textarea(
            attrs={
                'placeholder': '줄거리를 입력하세요.'
            }
        )
    )
    class Meta:
        model = Movie
        fields = ('title', 'title_en', 'audience', 'open_data', 'genre', 'watch_grade', 'score', 'poster_url', 'description')