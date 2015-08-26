from django import forms

from .models import Flipper, InventoryItem, PurchaseLot, SaleLot, Category

class RegisterForm(forms.ModelForm):

    class Meta:
        model = Flipper
        fields = ('first_name', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }

class LoginForm(forms.ModelForm):

    class Meta:
        model = Flipper
        fields = ('email', 'password',)
        widgets = {
            'password': forms.PasswordInput(),
        }

class ItemForm(forms.ModelForm):
    
	class Meta:
		model = InventoryItem
		fields = ('title', 'description', 'category', 'purchase_lot', 'purchase_price', 'purchase_date', 'purchase_medium', 'additional_expense', 
            'sale_lot', 'sale_price', 'sale_date', 'sale_medium')

class PurchaseLotForm(forms.ModelForm):
    
    class Meta:
        model = PurchaseLot
        fields = ('title', 'description', 'price', 'date', 'medium')

class SaleLotForm(forms.ModelForm):
    
    class Meta:
        model = SaleLot
        fields = ('title', 'description', 'price', 'date', 'medium')

class ManageForm(forms.ModelForm):

    # new_password = forms.CharField()
    # current_password = forms.CharField()

    class Meta:
        model = Flipper
        fields = ('first_name', 'email', 'app_title', 'app_theme')

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name', 'color')

