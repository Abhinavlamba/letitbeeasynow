from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])
class Content(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tosent = models.CharField(max_length=100, blank=True, default='')
    position = models.CharField(max_length=100, blank=True, default='')
    subject = models.CharField(max_length=100, blank=True, default='')
    matter = models.CharField(max_length=100, blank=True, default='')
    author = models.CharField(max_length=100, blank=True, default='')
    key = models.IntegerField(default=0)
    image = models.FileField(upload_to='1/',default='abcd/')
    def save(self, *args, **kwargs):
        super(Content, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created']
class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    position = models.CharField(max_length=100, blank=True, default='')
    department = models.CharField(max_length=100, blank=True, default='')
    user_details = models.CharField(max_length=100, blank=True, default='')
    contact = models.CharField(max_length=100, blank=True, default='')
    
    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        super(User, self).save(*args, **kwargs)
    class Meta:
        ordering = ['created']