from django.db import models

# Create your models here.

"""
   --- Home Page ---
1. Settings Model
--- banner video, banner title, banner slogan, about company, contact informations, social media accounts
2. Service Model
--- image, title, content
3. Our Work Model
--- image, title, content
4. Blog Model
--- image, title, content
5. Testimonial Model
6. Contact Model
"""

class SettingsModel(models.Model):
   banner_title = models.CharField("Banner başlığı", max_length=528, blank=True, null=True)
   banner_slogan = models.TextField("Banner sloqanı", blank=True, null=True)
   banner_video = models.FileField("Banner video", upload_to="bannervideo/", blank=True, null=True)
   about_company = models.TextField("Şirkət haqqında", blank=True, null=True)

   class Meta:
      verbose_name = "Parametr"
      verbose_name_plural = "Parametrlər"

   def __str__(self) -> str:
      return "Parametrlər"
   
class ContactInformationModel(models.Model):
   phone_number = models.CharField("Əlaqə nömrəsi", max_length=50, blank=True, null=True)
   email = models.EmailField("Email", max_length=256, blank=True, null=True)

   class Meta:
      verbose_name = "Əlaqə məlumatı"
      verbose_name_plural = "Əlaqə məlumatları"

   def __str__(self) -> str:
      contact_informations = ContactInformationModel.objects.all()
      return "Əlaqə məlumatı " + str(contact_informations.index(self) + 1)

class SocialMediaAccountModel(models.Model):
   name = models.CharField("Sosial media", max_length=256)
   link = models.URLField("Link", max_length=528)
   icon_name = models.CharField("Ikon", max_length=100)

   class Meta:
      verbose_name = "Sosial media hesabı"
      verbose_name_plural = "Sosial media hesabları"

   def __str__(self) -> str:
      return self.name

class ServiceModel(models.Model):
   image = models.ImageField("Şəkil", upload_to="service_images/")
   title = models.CharField("Başlıq", max_length=256)
   content = models.TextField("Məzmun", blank=True, null=True)

   class Meta:
      verbose_name = "Xidmət"
      verbose_name_plural = "Xidmətlər"

   def __str__(self) -> str:
      return self.title
   
class OurWorkModel(models.Model):
   image = models.ImageField("Şəkil", upload_to="ourwork_images/")
   title = models.CharField("Başlıq", max_length=256)
   content = models.TextField("Məzmun", blank=True, null=True)

   class Meta:
      verbose_name = "İş"
      verbose_name_plural = "İşlər"

   def __str__(self) -> str:
      return self.title
   
class BlogModel(models.Model):
   image = models.ImageField("Şəkil", upload_to="blog_images/")
   title = models.CharField("Başlıq", max_length=256)
   content = models.TextField("Məzmun", blank=True, null=True)

   class Meta:
      verbose_name = "Bloq"
      verbose_name_plural = "Bloqlar"

   def __str__(self) -> str:
      return self.title
   
class TestimonialModel(models.Model):
   image = models.ImageField("Şəkil", upload_to="testimonial_images/", blank=True, null=True)
   name = models.CharField("Ad", max_length=256)
   content = models.TextField("Məzmun")

   class Meta:
      verbose_name = "Testimonial"
      verbose_name_plural = "Testimoniallar"

   def __str__(self) -> str:
      return self.title
   
class ContactModel(models.Model):
   name = models.CharField("Ad", max_length=256)
   surname = models.CharField("Soyad", max_length=256)
   email = models.EmailField("Email", max_length=256)
   phone_number = models.CharField("Əlaqə nömrəsi", max_length=50)
   message = models.TextField("Mesaj")

   class Meta:
      verbose_name = "Mesaj"
      verbose_name_plural = "Mesajlar"

   def __str__(self):
      return self.name + " " + self.surname