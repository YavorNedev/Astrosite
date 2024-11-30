from django import forms
from astrosite.shop.models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'image', 'category']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


