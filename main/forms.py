from django import forms
from django.forms import inlineformset_factory

from .models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'

    def clean(self):
        cleaned_data = super().clean()
        forbidden_words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар')
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        for word in forbidden_words:
            if word in name.lower() or word in description.lower():
                raise forms.ValidationError(f"Запрещенное слово: {word}")

        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ('version_number', 'version_name', 'is_current',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'


VersionFormSet = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
