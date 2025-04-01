from django import forms
from .models import Events

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = '__all__'

    # Adding custom validation for each field if needed

    def clean_Title(self):
        title = self.cleaned_data.get('Title')
        if not title:
            raise forms.ValidationError("Title is required.")
        return title

    def clean_Description(self):
        description = self.cleaned_data.get('Description')
        if not description:
            raise forms.ValidationError("Description is required.")
        return description

    def clean_Location(self):
        location = self.cleaned_data.get('Location')
        if not location:
            raise forms.ValidationError("Location is required.")
        return location

    def clean_Date(self):
        event_date = self.cleaned_data.get('Date')
        if event_date < timezone.now():
            raise forms.ValidationError("Event date cannot be in the past.")
        return event_date
