from django import forms
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

from catalog.models import Product, Version, NULLABLE  # Sphere,


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'Submit'))
        # for field_name, field in self.fields.items():
        #     field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    Prohibited_Products = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']

    class Meta:
        model = Product
        # fields = '__all__'
        # fields = ('product_name', 'product_descr', 'product_category', 'product_price_each', 'email',)
        exclude = ('is_active', 'product_date_last', 'version_number', 'owner')


    # def clean_email(self):
    #     cleaned_data = self.cleaned_data['email']
    #
    #     if 'sky.pro' not in cleaned_data:
    #         raise forms.ValidationError('Почта должна быть только сотрудника компании SkyPro')
    #
    #     return cleaned_data

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name'].lower()
        for word in self.Prohibited_Products:
            if word in cleaned_data:
                raise forms.ValidationError('Запрещенное имя продукта')
        return cleaned_data

    def clean_product_descr(self):
        cleaned_data = self.cleaned_data['product_descr'].lower()
        for word in self.Prohibited_Products:
            if word in cleaned_data:
                raise forms.ValidationError('Запрещенные слова в описании продукта')
        return cleaned_data


# class SphereForm(StyleFormMixin, forms.ModelForm):
#
#     class Meta:
#         model = Sphere
#         fields = '__all__'


class VersionForm(StyleFormMixin, forms.ModelForm):
    ACTIVE_VERSIONS = []

    class Meta:
        model = Version
        fields = '__all__'

