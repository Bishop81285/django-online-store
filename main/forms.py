from django import forms
from django.forms import inlineformset_factory, BaseInlineFormSet

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

        if name:
            name = name.lower()
        if description:
            description = description.lower()

        for word in forbidden_words:
            if name and word in name or description and word in description:
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


class VersionFormSetCleaned(BaseInlineFormSet):
    def clean(self):
        super().clean()
        current_versions = [form.cleaned_data.get('is_current', False) for form in self.forms if
                            not form.cleaned_data.get('DELETE', False)]
        if current_versions.count(True) > 1:
            raise forms.ValidationError(
                'Может быть только одна активная версия продукта. Пожалуйста, выберите только одну.')


VersionFormSet = inlineformset_factory(Product, Version, form=VersionForm, formset=VersionFormSetCleaned, extra=1)
