from rest_framework import ModelSerializer 
from . models import CenteralBloodBank, BloodBankBranch, BloodBankSocialMediaUrl, Hospital, HospitalSocialMediaUrl


class CenteralBloodBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodType
        fields = ["blood_bank_name", "location", "email", "phone_number", "registered_date", "pan_number" ]

class BloodBankBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodBankBranch
        fields = ["main_branch", "blood_bank_name", "location", "email", "phone_number", "registered_date" ]

class BloodBankSocialMediaUrlSerializers(serializers.ModelSerializer):
    class Meta:
        model= BloodBankSocialMediaUrl
        fields = ["blood_bank", "facebook_url", "instagram_url", "youtube_url"]

class HospitalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ["hospital_name", "hospital_location", "email",  "phone_number", "pan_number"]
    
class HospitalSocialMediaUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalSocialMediaUrl
        fields = ["hospital", "facebook_url", "instagram_url", "youtube_url"]