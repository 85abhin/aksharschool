from django.db import models

# Create your models here.
# choices.py

INDIAN_STATES_CHOICES = [
    ('AP', 'Andhra Pradesh'),
    ('AR', 'Arunachal Pradesh'),
    ('AS', 'Assam'),
    ('BR', 'Bihar'),
    ('CT', 'Chhattisgarh'),
    ('GA', 'Goa'),
    ('GJ', 'Gujarat'),
    ('HR', 'Haryana'),
    ('HP', 'Himachal Pradesh'),
    ('JK', 'Jammu and Kashmir'),
    ('JH', 'Jharkhand'),
    ('KA', 'Karnataka'),
    ('KL', 'Kerala'),
    ('MP', 'Madhya Pradesh'),
    ('MH', 'Maharashtra'),
    ('MN', 'Manipur'),
    ('ML', 'Meghalaya'),
    ('MZ', 'Mizoram'),
    ('NL', 'Nagaland'),
    ('OR', 'Odisha'),
    ('PB', 'Punjab'),
    ('RJ', 'Rajasthan'),
    ('SK', 'Sikkim'),
    ('TN', 'Tamil Nadu'),
    ('TG', 'Telangana'),
    ('TR', 'Tripura'),
    ('UP', 'Uttar Pradesh'),
    ('UT', 'Uttarakhand'),
    ('WB', 'West Bengal'),
    ('AN', 'Andaman and Nicobar Islands'),
    ('CH', 'Chandigarh'),
    ('DN', 'Dadra and Nagar Haveli'),
    ('DD', 'Daman and Diu'),
    ('LD', 'Lakshadweep'),
    ('DL', 'Delhi'),
    ('PY', 'Puducherry')
]

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]

LANGUAGE_CHOICES = [
    ('EN', 'English'),
    ('HI', 'Hindi'),
    ('GU', 'Gujarati'),
]
# Model for Language choices
class Language(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class StudentRegistration(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, choices=INDIAN_STATES_CHOICES)
    zip_code = models.CharField(max_length=6)
    passport_photo = models.ImageField(upload_to='passport_photos/')
    signature = models.ImageField(upload_to='signatures/')
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class FeesAmount(models.Model):
    fees_Amount=models.FloatField(max_length=50)
    

class StudentFees(models.Model):
    mobile_number = models.ForeignKey(StudentRegistration, on_delete=models.CASCADE)
    fees=models.FloatField(max_length=50)
    is_paid = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.student.name} - {self.amount_due}"