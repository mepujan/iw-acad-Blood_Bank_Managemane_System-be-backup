from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models
from bank_hospital.models import BloodBankBranch, Hospital
User = get_user_model()
blood_types = (
    ('O+', 'O-Positive'), ('O-', 'O-Negative'), ('A+', 'A-Positive'), ('A-', 'A-Negative'), ('B+', 'B-Positive'),
    ('B-', 'B-Negative'), ('AB+', 'AB-Positive'), ('AB-', 'AB-Negative'))
sponsor_type = (('personal', 'personal'), ('organizational', 'organizational'))


class BloodType(models.Model):
    blood_type = models.CharField(max_length=10, choices=blood_types)

    def __str__(self):
        return self.blood_type


class Sponsor(models.Model):
    sponsor_name = models.CharField(max_length=200)
    sponsor_email = models.EmailField(unique=True)
    sponsor_amount = models.FloatField()
    sponsor_type = models.CharField(max_length=14, choices=sponsor_type)
    phone_number = models.CharField(max_length=15)
    sponsor_address = models.CharField(max_length=50)

    def __str__(self):
        return self.sponsor_name


class Campaign(models.Model):
    blood_bank = models.ForeignKey(BloodBankBranch, on_delete=models.CASCADE)
    campaign_name = models.CharField(max_length=200)
    campaign_location = models.CharField(max_length=100)
    campaign_start_date_time = models.DateTimeField()
    campaign_end_date_time = models.DateTimeField()
    campaign_host_name = models.CharField(max_length=200)
    sponsor = models.ManyToManyField(Sponsor)
    about_campaign = RichTextField()
    campaign_image = models.ImageField(upload_to='campaign_image')

    def __str__(self):
        return self.campaign_name


class Volunteer(models.Model):
    volunteer_name = models.CharField(max_length=100)
    volunteer_address = models.CharField(max_length=100)
    volunteer_mobile_number = models.CharField(max_length=15)
    volunteer_role = models.CharField(max_length=20)
    register_for_campaign = models.ForeignKey(Campaign, on_delete=models.DO_NOTHING)
    volunteer_profile_pic = models.ImageField(upload_to='volunteer_profile')

    def __str__(self):
        return self.volunteer_name


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField()
    feature_image = models.ImageField(upload_to='featured_image')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class CollectedBlood(models.Model):
    collected_date = models.DateField()
    collected_from_campaign = models.ForeignKey(Campaign, on_delete=models.DO_NOTHING)
    a_positive = models.IntegerField(null=True)
    a_negative = models.IntegerField(null=True)
    o_positive = models.IntegerField(null=True)
    o_negative = models.IntegerField(null=True)
    b_positive = models.IntegerField(null=True)
    b_negative = models.IntegerField(null=True)
    ab_positive = models.IntegerField(null=True)
    ab_negative = models.IntegerField(null=True)

    def total_num_blood_collected(self):
        total_collection = self.a_positive + self.a_negative + self.ab_negative + self.ab_positive + self.o_negative + \
                           self.o_positive + self.b_negative + self.b_positive
        return total_collection

    def __str__(self):
        return self.collected_date


class Discussion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = RichTextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class BloodPacket(models.Model):
    packet_num = models.CharField(max_length=50, unique=True)
    blood_type = models.ForeignKey(BloodType, on_delete=models.DO_NOTHING)
    blood_bank = models.ForeignKey(BloodBankBranch, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.DO_NOTHING)
    expire_date = models.DateField()

    def __str__(self):
        return self.packet_num


# class BloodStock(models.Model):
#     blood_bank = models.ForeignKey(BloodBank, on_delete=models.CASCADE)
#     a_positive = models.IntegerField(null=True)
#     a_negative = models.IntegerField(null=True)
#     o_positive = models.IntegerField(null=True)
#     o_negative = models.IntegerField(null=True)
#     b_positive = models.IntegerField(null=True)
#     b_negative = models.IntegerField(null=True)
#     ab_positive = models.IntegerField(null=True)
#     ab_negative = models.IntegerField(null=True)
#
#     def __str__(self):
#         return self.blood_bank.blood_bank_name


class BloodRequest(models.Model):
    request_from = models.ForeignKey(Hospital, on_delete=models.DO_NOTHING)
    request_to = models.ManyToManyField(BloodBankBranch)
    request_date = models.DateField()
    amount_of_blood = models.IntegerField()
    blood_type_requested = models.ManyToManyField(BloodType)

    def __str__(self):
        return self.request_from.hospital_name
