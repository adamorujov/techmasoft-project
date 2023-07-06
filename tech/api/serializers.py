from rest_framework import serializers
from tech.models import (
    SettingsModel, ContactInformationModel, SocialMediaAccountModel,
    ServiceModel, OurWorkModel, BlogModel, TestimonialModel, ContactModel
)

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettingsModel
        fields = "__all__"

class ContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformationModel
        fields = "__all__"

class SocialMediaAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaAccountModel
        fields = "__all__"

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = "__all__"

class OurWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurWorkModel
        fields = "__all__"

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = "__all__"

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestimonialModel
        fields = "__all__"

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = "__all__"
