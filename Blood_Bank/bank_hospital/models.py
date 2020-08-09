from django.db import models


class CenteralBloodBank(models.Model):
    blood_bank_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12)
    registered_date = models.DateField()
    pan_number = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.email


class BloodBankBranch(models.Model):
    main_branch = models.ForeignKey(CenteralBloodBank, on_delete=models.CASCADE)
    blood_bank_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12)
    registered_date = models.DateField()

    def __str__(self):
        return self.blood_bank_name

    class Meta:
        verbose_name_plural = 'BloodBankBranches'


class BloodBankSocialMediaUrl(models.Model):
    blood_bank = models.OneToOneField(BloodBankBranch, on_delete=models.CASCADE)
    facebook_url = models.URLField(null=True, unique=True)
    instagram_url = models.URLField(null=True, unique=True)
    youtube_url = models.URLField(null=True, unique=True)


class Hospital(models.Model):
    hospital_name = models.CharField(max_length=100)
    hospital_location = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12)
    pan_number = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.email


class HospitalSocialMediaUrl(models.Model):
    hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE)
    facebook_url = models.URLField(null=True, unique=True)
    instagram_url = models.URLField(null=True, unique=True)
    youtube_url = models.URLField(null=True, unique=True)
