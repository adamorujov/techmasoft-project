from django.urls import path
from tech.api import views

urlpatterns = [
    path('settings/', views.SettingsListAPIView.as_view(), name="settings"),
    path('contactinformations/', views.ContactInformationListAPIView.as_view(), name="contactinformations"),
    path('socialmediaaccounts/', views.SocialMediaAccountListAPIView.as_view(), name="socialmediaaccounts"),
    path('services/', views.ServiceListAPIView.as_view(), name="services"),
    path('ourworks/', views.OurWorkListAPIView.as_view(), name="ourworks"),
    path('blogs/', views.BlogListAPIView.as_view(), name="blogs"),
    path('testimonials/', views.TestimonialListAPIView.as_view(), name="testimonials"),
    path('messages/', views.ContactListAPIView.as_view(), name="messages"),
    path('message-create/', views.ContactCreateAPIView.as_view(), name="message-create"),

]