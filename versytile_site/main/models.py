from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

# Create your models here.
class Forum(models.Model):
    title= models.CharField(max_length=200)
    subtitle= models.CharField(max_length=200,default="", blank=True)
    slug = models.SlugField("Forum Slug", null=False,blank = False, unique = True)
    published = models.DateTimeField("Date published", default= timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Forums"
        ordering = ['published']


class Discussion(models.Model):
    title= models.CharField(max_length=200)
    subtitle= models.CharField(max_length=200,default="", blank=True)
    Discussion_slug = models.SlugField("Discussion Slug", blank=False, null=False, unique = True)
    content= HTMLField(blank=True, default="")
    notes=HTMLField(blank=True, default="")
    published = models.DateTimeField("Date published", default= timezone.now)
    modified = models.DateTimeField("Date published", default= timezone.now)
    a_forum = models.ForeignKey(Forum, default="", verbose_name= "Forums", on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.title
    
    @property
    def slug(self):
        return self.a_forum.slug + "/" + self.Discussion_slug

    class Meta:
        verbose_name_plural = "Discussion"
        ordering = ['published']
    


