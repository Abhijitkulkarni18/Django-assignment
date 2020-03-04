from django.db import models
from Auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import JSONField

# Create your models here.
class Document(models.Model):
    source_id = models.CharField(null=True, blank=True,max_length=50)
    type = models.CharField(max_length=100)
    owner = models.ForeignKey(User,related_name='document_owner',on_delete=models.CASCADE)
    input_meta_data = JSONField(null=True, blank=True,default=dict)
    SOURCE_CHOICES = (("NEWSPAPER", _("Newspaper")),("SOCIALMEDIA", _("socialmedia")))
    source_type=models.CharField(choices=SOURCE_CHOICES,null=True, blank=True,max_length=20)
    created_time = models.DateTimeField(auto_now_add=True)
    
    def __self__(self):
        return self.type

    def __str__(self):
        return self.type
