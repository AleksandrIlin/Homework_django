from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    """Форма модели продукт"""
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название продукта'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание продукта'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите стоимость продукта'
        })

    def clean_price(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')

        if price is None:
            raise forms.ValidationError('Стоимость продукта должна быть указана.')

        if price < 0:
            raise forms.ValidationError('Цена продукта не может быть отрицательной.')

        return price

    def clean_image(self):
        cleaned_data = super().clean()
        image = cleaned_data.get('image')

        if image.size > 5 * 1024 * 1024:
            raise forms.ValidationError('Размер файла не должен превышать 5MB.')

        if image.name.endswith(('jpg', 'jpeg', 'png')):
            raise forms.ValidationError('Формат файла не соответствует требованиям. '
                                        'Формат файла должен быть *.jpg, *.jpeg, *.png')

        return image

