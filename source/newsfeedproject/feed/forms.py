from django import forms
from .models import Novelty

class NoveltyForm(forms.ModelForm):
    class Meta:
        model = Novelty
        fields = ('title', 'text',)

class NoveltyFormForEdit(NoveltyForm):
    class Meta(NoveltyForm.Meta):
        fields = '__all__'
