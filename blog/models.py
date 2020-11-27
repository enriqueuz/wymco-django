''' Blog models '''

# Django
from django.db import models

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

def post_images_path(instance, filename):
    # Path images function 
    image_path = f'post_images/{instance.slug}/{filename}'
    return image_path

class BlogPost(models.Model):
    ''' Post model. '''

    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to=post_images_path, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
