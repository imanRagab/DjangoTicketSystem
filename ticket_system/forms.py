from django import forms
from ticket_system.models import Ticket


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = (
            'ticket_title',
            'ticket_description',
            'ticket_user_email',
        )

        widgets = {
            'ticket_title': forms.TextInput(attrs={
                'id': 'title',
                'required': True,
                'class': "form-control",
            }),
            'ticket_description': forms.Textarea(attrs={
                'id': 'description',
                'required': True,
                'class': "form-control",
            }),
            'ticket_user_email': forms.TextInput(attrs={
                'id': 'email',
                'required': True,
                'class': "form-control",
            }),
        }


