from django.contrib import admin
from tech.models import (
    SettingsModel, ContactInformationModel, SocialMediaAccountModel,
    ServiceModel, OurWorkModel, BlogModel, TestimonialModel, ContactModel
)
from django.contrib.admin.sites import AdminSite

AdminSite.site_header = 'Techmasoft administrasiyası'
AdminSite.site_title = 'Techmasoft sayt administratoru'

admin.site.register(SettingsModel)
admin.site.register(ContactInformationModel)
admin.site.register(SocialMediaAccountModel)
admin.site.register(ServiceModel)
admin.site.register(OurWorkModel)
admin.site.register(BlogModel)
admin.site.register(TestimonialModel)
admin.site.register(ContactModel)

