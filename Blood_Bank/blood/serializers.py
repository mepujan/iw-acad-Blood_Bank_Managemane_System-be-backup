from rest_framework import serializers
from .models import (BloodType, Sponsor, Campaign,
                     Volunteer, Announcement, CollectedBlood,
                     Discussion,
                     BloodPacket, BloodRequest)


class BloodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodType
        fields = ['blood_type']


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'


class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = '__all__'


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'


class CollectedBloodSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectedBlood
        fields = '__all__'


class DiscussionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discussion
        fields = '__all__'


class BloodPacketSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodPacket
        fields = '__all__'


class BloodRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodRequest
        fields = '__all__'
