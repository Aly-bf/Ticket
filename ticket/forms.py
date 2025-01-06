from django import forms
from .models import Ticket, Message

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['subject', 'description', 'file']
        widgets = {
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter your subject',
                'style': 'max-width: 300px',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'enter your subject',
                'style': 'max-width: 300px',
            })
            
        }

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['ticket']