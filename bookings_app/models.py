from django.db import models

# Create your models here.
from events_app.models import Event

class Participant(models.Model):
    first_name = models.CharField(max_length=100, help_text="First name of the participant, max. 100 characters.")
    last_name = models.CharField(max_length=100, help_text="Last name of the participant, max. 100 characters.")
    fullname = models.CharField(max_length=200, blank=True, help_text="Full name of the participant, auto-generated.")
    email = models.EmailField(unique=True, help_text="Email address of the participant, must be unique and valid.")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.participant} → {self.event.title}"