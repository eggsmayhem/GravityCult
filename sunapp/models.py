from django.db import models

#added for ck
from ckeditor.fields import RichTextField 

PARK_CHOICES = (
    #('Difficult Run, Virginia', 'Difficult Run, Virginia'),
    #('Reston', 'Reston'),
    #('Cherry Blossum Tree, D.C.', 'Cherry Blossum Tree, D.C.',),
    ('Cleveland, OH', 'Cleveland, OH'),
    ('Columbus, OH', 'Columbus, OH'),
    ('Northern VA', 'Northern VA'),
    ('Oakland, CA', 'Oakland, CA'),
)

class Image(models.Model):
    location = models.CharField(max_length=40, choices=PARK_CHOICES, default='Columbus, OH')
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, default="anonymous")
    image = models.ImageField(upload_to='images', blank=True)
    #def image(self):
    #    if self.image and hasattr(self.image, 'url'):
    #        return self.image.url
    created_on = models.DateTimeField(auto_now = True)
    #added for ck
    content = RichTextField(blank=True, null=True)
    def __str__(self):
        return self.title
    class Meta:
        db_table = "myapp_image"
        ordering = ['-created_on']

 