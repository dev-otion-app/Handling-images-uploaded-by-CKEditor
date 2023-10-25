from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title = models.CharField(max_length = 250)
    content = RichTextUploadingField()

    def __str__(self):
        return self.title

class CKEditorPostImages(models.Model):
    name = models.CharField(max_length=250)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)