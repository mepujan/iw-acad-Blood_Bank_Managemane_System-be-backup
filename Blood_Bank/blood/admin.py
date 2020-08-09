from django.contrib import admin

from .models import Campaign, CollectedBlood, Announcement, Volunteer, Discussion, Sponsor, BloodPacket, BloodType

admin.site.site_header = 'Blood Bank'
admin.site.register(Campaign)
admin.site.register(CollectedBlood)
admin.site.register(Announcement)
admin.site.register(Volunteer)
admin.site.register(Discussion)
admin.site.register(Sponsor)
admin.site.register(BloodPacket)
admin.site.register(BloodType)
