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


