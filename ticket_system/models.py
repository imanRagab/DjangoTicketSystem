from django.db import models

class Ticket(models.Model):

    PENDING = 0;
    RESOLVED = 1;

    STATE_CHOICES = (
        (PENDING, 'Pending'),
        (RESOLVED, 'Resolved'),
    )

    ticket_title = models.CharField(max_length=255);
    ticket_description = models.TextField();
    ticket_user_email = models.EmailField(max_length=255);
    ticket_status = models.IntegerField(
        max_length=255,
        choices=STATE_CHOICES,
        default=PENDING,
    );
    ticket_created_at = models.DateTimeField(auto_now_add=True, blank=True);


    def __str__(self):
        return self.ticket_title;

