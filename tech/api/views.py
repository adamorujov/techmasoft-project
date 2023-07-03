from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser
from tech.models import (
    SettingsModel, ContactInformationModel, SocialMediaAccountModel,
    ServiceModel, OurWorkModel, BlogModel, TestimonialModel, ContactModel
)
from tech.api.serializers import (
    SettingsSerializer, ContactInformationSerializer, SocialMediaAccountSerializer,
    ServiceSerializer, OurWorkSerializer, BlogSerializer, TestimonialSerializer, ContactSerializer
)

class SettingsListAPIView(ListAPIView):
    queryset = SettingsModel.objects.all()
    serializer_class = SettingsSerializer

class ContactInformationListAPIView(ListAPIView):
    queryset = ContactInformationModel.objects.all()
    serializer_class = ContactInformationSerializer

class SocialMediaAccountListAPIView(ListAPIView):
    queryset = SocialMediaAccountModel.objects.all()
    serializer_class = SocialMediaAccountSerializer

class ServiceListAPIView(ListAPIView):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer

class OurWorkListAPIView(ListAPIView):
    queryset = OurWorkModel.objects.all()
    serializer_class = OurWorkSerializer

class BlogListAPIView(ListAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer

class TestimonialListAPIView(ListAPIView):
    queryset = TestimonialModel.objects.all()
    serializer_class = TestimonialSerializer

class ContactListAPIView(ListAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsAdminUser,)

class ContactCreateAPIView(CreateAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer