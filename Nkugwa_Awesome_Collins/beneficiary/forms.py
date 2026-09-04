from django import forms
from django.utils import timezone
from .models import Beneficiary


class BeneficiaryForm(forms.ModelForm):
    class Meta:
        model = Beneficiary
        fields = [
            'first_name', 'last_name', 'date_of_birth', 'place_of_birth',
            'gender', 'nationality', 'marital_status',
            'settlement_camp', 'date_joined_camp',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your First name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your Last name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY / MM / DD'}),
            'place_of_birth': forms.TextInput(attrs={'placeholder': 'Enter your place of residence'}),
            'gender': forms.RadioSelect,
            'date_joined_camp': forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY / MM / DD'}),
        }

    def clean_first_name(self):
        value = self.cleaned_data['first_name']
        if len(value.strip()) < 2:
            raise forms.ValidationError("Invalid field")
        return value

    def clean_last_name(self):
        value = self.cleaned_data['last_name']
        if len(value.strip()) < 2:
            raise forms.ValidationError("Invalid field")
        return value

    def clean_place_of_birth(self):
        value = self.cleaned_data['place_of_birth']
        if len(value.strip()) < 2:
            raise forms.ValidationError("Invalid field")
        return value

    def clean_date_of_birth(self):
        value = self.cleaned_data['date_of_birth']
        today = timezone.now().date()
        if value >= today:
            raise forms.ValidationError("Invalid field")
        return value

    def clean_date_joined_camp(self):
        value = self.cleaned_data['date_joined_camp']
        today = timezone.now().date()
        if value <= today:
            raise forms.ValidationError("Invalid field")
        return value