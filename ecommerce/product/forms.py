from django import forms
from .models import product


class productform(forms.ModelForm):

	class Meta:
		model = product
		fields = ('Name','Description','Seller_Mobile','Price_Range')



	def __init__(self, *args, **kwargs):
		super(productform,self).__init__(*args, **kwargs)
		self.fields['Price_Range'].empty_label = "Select"



