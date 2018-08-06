from django import forms

from .models import Gallery


class GalleryForm(forms.ModelForm):
    """
    Base form for gallery uploads
    """
    bulk_upload = forms.FileField(
        widget=forms.FileInput(attrs={'multiple': 'multiple'}),
        required=False
    )

    class Meta:
        model = Gallery
        fields = ['overline', 'title', 'slug', 'credit', 'summary', 'published', 'bulk_upload']
 