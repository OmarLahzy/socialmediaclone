from django.db import models
from django.conf import settings
from django.urls import reverse
from groups.models import Group
from django.contrib.auth import get_user_model
USER = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(USER,related_name='posts',on_delete=models.CASCADE)
    createat = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group,related_name='posts',null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.message
    def get_absloute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk})
    class Meta:
        ordering = ['-createat']
        unique_together = ['user','message']
