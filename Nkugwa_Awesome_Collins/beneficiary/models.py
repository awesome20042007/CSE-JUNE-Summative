from django.db import models


# Create your models here.
class Beneficiary(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    NATIONALITY_CHOICES = [
        ('Ugandan', 'Ugandan'),
        ('Kenyan', 'Kenyan'),
        ('Tanzanian', 'Tanzanian'),
        ('Burundian', 'Burundian'),
        ('Rwandese', 'Rwandese'),
        ('Somali', 'Somali'),
        ('South Sudanese', 'South Sudanese'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
        ('Separated', 'Separated'),
    ]

    SETTLEMENT_CAMP_CHOICES = [
        ('Gulu settlement camp', 'Gulu settlement camp'),
        ('Arua settlement camp', 'Arua settlement camp'),
        ('Mbarara settlement camp', 'Mbarara settlement camp'),
        ('Kasese settlement camp', 'Kasese settlement camp'),
        ('Busia settlement camp', 'Busia settlement camp'),
        ('Mbale settlement camp', 'Mbale settlement camp'),
        ('Kigezi settlement camp', 'Kigezi settlement camp'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=150)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Female')
    nationality = models.CharField(max_length=30, choices=NATIONALITY_CHOICES)
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS_CHOICES)
    settlement_camp = models.CharField(max_length=40, choices=SETTLEMENT_CAMP_CHOICES)
    date_joined_camp = models.DateField()
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"