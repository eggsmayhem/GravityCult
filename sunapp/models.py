from django.db import models

#added for ck
from ckeditor.fields import RichTextField 

class Image(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, default="anonymous")
    image = models.ImageField(upload_to='images')
    created_on = models.DateTimeField(auto_now = True)
    #added for ck
    content = RichTextField(blank=True, null=True)
    def __str__(self):
        return self.title
    class Meta:
        db_table = "myapp_image"
        ordering = ['-created_on']

 