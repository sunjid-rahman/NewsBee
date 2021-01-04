from django.db import models
from accounts.models import User
from django.conf import settings
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.

class SharedNews(models.Model):
    author=models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    source=models.CharField(max_length=255)
    category=models.CharField(max_length=255,blank=True,null=True)
    image=models.CharField(max_length=255,blank=True,null=True)
    description=models.TextField(blank=True,default='')
    created_at=models.DateTimeField(auto_now=False)
    shared_by=models.ForeignKey(User,related_name='sharedUser',null=True,blank=True,on_delete=models.CASCADE)
    shared_views=models.TextField(blank=True,null=True,default='')
    # slug=models.SlugField(allow_unicode=True,unique=True,default='')
    shared_date=models.DateTimeField(blank=True, null=True)
    def save(self,*args,**kwargs):
        # self.slug=slugify(self.title)
        self.shared_date=timezone.now()
        super().save(*args,**kwargs)
        def get_absolute_url(self):
            return reverse('news:news_list',kwargs={'pk':self.pk})
        class Meta:
            ordering=['-shared_date']
