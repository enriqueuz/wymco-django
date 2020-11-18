''' Blog models '''

# Django
from django.db import models

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

class BlogPost(models.Model):
    ''' Post model. '''

    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
