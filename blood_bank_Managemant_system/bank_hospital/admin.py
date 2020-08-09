from django.contrib import admin

from .models import BloodBankBranch,CenteralBloodBank, BloodBankSocialMediaUrl, Hospital, HospitalSocialMediaUrl

admin.site.register(CenteralBloodBank)
admin.site.register(BloodBankBranch)
admin.site.register(BloodBankSocialMediaUrl)
admin.site.register(Hospital)
admin.site.register(HospitalSocialMediaUrl)
