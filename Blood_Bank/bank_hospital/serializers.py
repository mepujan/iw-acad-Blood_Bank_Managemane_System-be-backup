from rest_framework import serializers
from .models import (CenteralBloodBank, BloodBankBranch,
                     BloodBankSocialMediaUrl, Hospital, HospitalSocialMediaUrl)


class CentralBloodBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = CenteralBloodBank
        fields = '__all__'


class BloodBankLBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodBankBranch
        fields = '__all__'


class BloodBankSocialMediaUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodBankSocialMediaUrl
        fields = '__all__'


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'


class HospitalSocialMediaUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalSocialMediaUrl
        fields = '__all__'

