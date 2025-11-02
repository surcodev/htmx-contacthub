from django import forms
from .models import Contact



class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input input-bordered w-full',
            'placeholder': 'Contact Name'
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'input input-bordered w-full',
            'placeholder': 'Email Address'
        })
    )    

    def clean_name(self):
        name = self.cleaned_data['name']
        if name.startswith('X'):
            raise forms.ValidationError("Name cannot start with a X!")
        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        # Ensure email is unique
        if Contact.objects.filter(user=self.initial.get('user'), email=email).exists():
            raise forms.ValidationError("A contact with this email already exists.")
        return email

    class Meta:
        model = Contact
        fields = (
            'name', 'email'
        )