from django import forms
from .models import Registration,Author,Book

class UserRegistration(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name','email','password']
        widgets = {
            'name':forms.TextInput(),
            'email':forms.EmailInput(),
            'password':forms.PasswordInput()
        }
        
class loginchecking(forms.Form):
    email = forms.EmailField(label="Enter Email")
    password = forms.CharField(label="Enter Password",widget=forms.PasswordInput)
    
class AuthorRegistration(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name','address']
        widgets = {
            'name':forms.TextInput(),
            'address':forms.TextInput()
        }
        
class BookRegistration(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name','isbn','price']
        widgets = {
            'name':forms.TextInput(),
            'isbn':forms.NumberInput(),
            'price':forms.NumberInput()
        }