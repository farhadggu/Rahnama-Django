from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from translated_fields import TranslatedField
from django.utils.translation import gettext_lazy as _



class Settings(models.Model):
    name = TranslatedField(models.CharField(_("نام سایت"), max_length=100, blank=True, help_text="کادر اول فارسی کادر دوم انگلیسی"))
    address = TranslatedField(models.CharField(_("آدرس بنیاد"), max_length=300, blank=True, help_text="کادر اول فارسی کادر دوم انگلیسی"))
    phone_number = models.CharField(_("شماره تماس"), max_length=20, blank=True)
    phone_number2 = models.CharField(_("شماره تماس 2"), max_length=20, blank=True)
    email = models.CharField(_("ایمیل"), max_length=50, blank=True)
    description_footer = TranslatedField(models.CharField(_("توضیحات فوتر"), max_length=300, blank=True, help_text="کادر اول فارسی کادر دوم انگلیسی"))
    instagram = models.URLField(_("اینستاگرام"), blank=True)
    telegram = models.URLField(_("تلگرام"), blank=True)
    whatsapp = models.URLField(_("واتساپ"), blank=True)
    linkdin = models.URLField(_("لینکدین"), blank=True)
    about_company = TranslatedField(RichTextUploadingField(_("درباره بنیاد"), help_text="کادر اول فارسی کادر دوم انگلیسی"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("تنظیمات")
        verbose_name_plural = _("تنظیمات")