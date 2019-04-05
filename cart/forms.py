from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 6)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(label='', choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, widget=forms.HiddenInput)
