#Library Import
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _
from translated_fields import TranslatedField
from django.utils.html import format_html
from django.urls import reverse
from django.db import models


class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStamp):
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name="children", verbose_name=_("زیر مجموعه"))
    is_sub = models.BooleanField(_("این دسته بندی فرزند میباشد؟"), default=False)
    title = TranslatedField(models.CharField(_("تیتر دسته بندی"), max_length=100, help_text="کادر اول فارسی کادر دوم انگلیسی"))
    slug = models.SlugField(_("نام دسته بندی در لینک(اسلاگ)"), max_length=100)
    # Post Models
    title_post = TranslatedField(models.CharField(_("تیتر مقاله"), max_length=200, help_text="کادر اول فارسی کادر دوم انگلیسی", blank=True))
    desc_post =  TranslatedField(RichTextUploadingField(_("توضیحات مقاله"), help_text="کادر اول فارسی کادر دوم انگلیسی", blank=True))
    img_post = models.ImageField(_("تصویر مقاله"), upload_to='media', blank=True, null=True)
    video_post = models.URLField(_("لینک کد امبد آپارات"), max_length=500, blank=True, null=True)
    file = models.FileField(_("آپلود فایل"), upload_to="documents" ,blank=True, null=True)

    class Meta:
        verbose_name = _("دسته بندی")
        verbose_name_plural = _("دسته بندی ها")
        ordering = ('created',)

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::1])

    def get_absolute_url(self):
        return reverse('posts:category_detail', args=(self.slug,))


class Post(TimeStamp):
    STATUS = (
        ('p', 'منتشر شده'),
        ('d', 'پیش نویس'),
    )

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, related_name="articles", verbose_name=_("دسته بندی"))
    title = TranslatedField(models.CharField(_("تیتر مقاله"), max_length=200, help_text="کادر اول فارسی کادر دوم انگلیسی"))
    slug = models.SlugField(_("نام مقاله در لینک (اسلاگ)"), )
    desc =  TranslatedField(RichTextUploadingField(_("توضیحات مقاله"), help_text="کادر اول فارسی کادر دوم انگلیسی"))
    img = models.ImageField(_("تصویر"), upload_to='media', blank=True, null=True)
    video = models.URLField(_("لینک کد امبد آپارات"), max_length=500, blank=True, null=True)
    status = models.CharField(_("وضعیت انتشار"), max_length=1, choices=STATUS)
    vip = models.BooleanField(_("اسلاید خدمات می باشد؟"), default=False, help_text='فقط 2 اسلاید میتوان اختصاص داد')

    class Meta:
        verbose_name = _("مقاله")
        verbose_name_plural = _("مقالات")
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:post_detail', args=(self.slug,))

    def img_tag(self):
        return format_html('<img src="{}" width=100px />'.format(self.img.url))
    img_tag.short_description = "تصویر مقاله"