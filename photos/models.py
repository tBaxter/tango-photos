from django.conf import settings
from django.db import models
from django.urls import reverse

from .managers import GalleryManager, PublishedGalleryManager
from tango_shared.models import ContentImage, BaseContentModel

supports_articles = 'articles' in settings.INSTALLED_APPS


class Gallery(BaseContentModel):
    """
    Allows for Gallery creation.
    If you get a "413 Entity Too Large" error when bulk uploading, adjust the Nginx configuration. 

    """
    credit = models.CharField(max_length=200, blank=True)
    published = models.BooleanField(default=True)
    
    if supports_articles:
        article = models.ForeignKey(
            'articles.Article',
            on_delete=models.CASCADE,
            blank=True,
            null=True
        )

    # Managers
    objects = GalleryManager()
    published_objects = PublishedGalleryManager()

    class Meta:
        verbose_name_plural = "galleries"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gallery_detail', self.slug)

    def get_image(self):
        try:
            return self.galleryimage_set.all()[0]
        except IndexError:
            return None


class GalleryImage(ContentImage):
    gallery = models.ForeignKey(
        Gallery,
        on_delete=models.CASCADE
    )
