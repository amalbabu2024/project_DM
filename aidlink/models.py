from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_civilian = models.BooleanField(default=False)
    is_coordinator = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        roles = []
        if self.is_civilian:
            roles.append('Civilian')
        if self.is_coordinator:
            roles.append('Coordinator')
        if self.is_admin:
            roles.append('Admin')
        return f"{self.username} ({', '.join(roles)})"

class Civilian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='civilian')
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    country = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=10, null=True)
    profile_photo = models.ImageField(blank=True, null=True, upload_to='civilian_profile_photos/')
    email = models.EmailField(max_length=254, default='default@email.com')

    def __str__(self):
        return self.user.username

class Coordinator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='coordinator')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    contact_email = models.EmailField(max_length=254)
    contact_phone_number = models.CharField(max_length=15)
    profile_photo = models.ImageField(blank=True, null=True, upload_to='coordinator_profile_photos/')
    verification = models.CharField(max_length=20, default='Pending')
    registered_through_form = models.BooleanField(default=True)
    email = models.EmailField(max_length=254, default='default@email.com')

    def __str__(self):
        return self.user.username

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='admin')

    def __str__(self):
        return self.user.username




class Resource(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=50, blank=True)
    quantity = models.CharField(max_length=100, blank=True)  # Changed to accept text and integer
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    

class Camp(models.Model):
    camp_id = models.AutoField(primary_key=True)
    camp_name = models.CharField(max_length=100)
    camp_location = models.CharField(max_length=100, blank=True)
    capacity = models.IntegerField()
    contact_phone = models.CharField(max_length=15)
    contact_email = models.EmailField(max_length=254)

    def __str__(self):
        return self.camp_name




class MarkedLocation(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name




from django.contrib.auth import get_user_model

class Message(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    priority_choices = [
        ('Urgent', 'Urgent/High Priority'),
        ('Important', 'Important/Action Required'),
        ('Informational', 'Informational/Update'),
        ('Decision', 'Decision/Approval Needed'),
        ('Routine', 'Routine/General Communication'),
        ('FYI', 'FYI/Information Only'),
        ('Acknowledgment', 'Acknowledgment/Confirmation'),
        ('Appreciation', 'Appreciation/Recognition'),
        ('Miscellaneous', 'Miscellaneous/Other'),
    ]
    priority = models.CharField(max_length=20, choices=priority_choices, default='Informational')
    category = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.priority} - {self.category}"




from django.conf import settings
from django.utils import timezone
from django.db import models

class HelpRequest(models.Model):
    REQUEST_STATUS_CHOICES = (
        (0, 'Request Sent'),
        (1, 'Request Received'),
        (2, 'Request Processing'),
        (3, 'Request Completed'),
        (4, 'Request Rejected'),
    )

    civilian = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    request_type = models.CharField(max_length=50)
    urgency_level = models.CharField(max_length=20, blank=True, null=True)
    people_affected = models.IntegerField(blank=True, null=True)
    details = models.TextField()
    attachments = models.FileField(upload_to='help_request_attachments/', blank=True, null=True)
    language_preference = models.CharField(max_length=50, blank=True)
    special_needs = models.CharField(max_length=100, blank=True)
    incident_datetime = models.DateTimeField(default=timezone.now)
    relationship_to_situation = models.CharField(max_length=100, blank=True, null=True)
    confirmation_checkbox = models.BooleanField(default=False)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    current_location = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    request_status = models.IntegerField(choices=REQUEST_STATUS_CHOICES, default=0)

    def get_request_status_display(self):
        return dict(self.REQUEST_STATUS_CHOICES).get(self.request_status, 'Unknown')

    def __str__(self):
        return f"{self.name} - {self.request_type} - {self.timestamp}"







# models.py
from django.db import models
from django.contrib.auth import get_user_model

class VolunteerRequest(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    full_name = models.TextField(default='')
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.TextField(default='')
    address = models.TextField(default='')
    phone_mobile = models.TextField(default='')
    email = models.EmailField(default='')
    emergency_contact_name = models.TextField(default='')
    emergency_contact_phone = models.TextField(default='')
    relevant_skills_medical = models.BooleanField(default=False)
    relevant_skills_technical = models.BooleanField(default=False)
    certifications_first_aid = models.BooleanField(default=False)
    previous_experience = models.TextField(default='')
    educational_qualifications = models.TextField(default='')
    blood_group = models.CharField(max_length=5, default='')  # Assuming blood group as a string
    health_condition = models.TextField(default='')
    status = models.CharField(max_length=20, default='Pending')  # 'Pending', 'Approved', 'Rejected'

    def __str__(self):
        return f"{self.user.username} - {self.status}"

