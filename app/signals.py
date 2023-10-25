from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db.models import Q
from .models import Post, CKEditorPostImages
from .utils import delete_images
import re

@receiver(pre_save, sender=Post)
def pre_save_post(sender, **kwargs):
    instance = kwargs['instance']
    try:
        excluded_images = CKEditorPostImages.objects.filter(Q(post = Post.objects.get(id=instance.id)) & ~Q(name__in = [name for name in re.findall('<img.*src=".*ckeditor/([^"]+)', instance.content)]))
        if excluded_images.exists():
            excluded_images.update(post=None)
    except Post.DoesNotExist:
        pass

@receiver(post_save, sender=Post)
def post_save_post(sender, **kwargs):
    instance = kwargs['instance']
    images = re.findall('<img.*src=".*ckeditor/([^"]+)', instance.content)
    db_image_recorder = CKEditorPostImages.objects.filter(Q(name__in = images) & Q(post__isnull=True))
    db_image_recorder.update(post=Post.objects.get(id = instance.id))
    orphan_images = CKEditorPostImages.objects.filter(post__isnull = True)
    for image in orphan_images:
        delete_images('/media/ckeditor/' + image.name)
    orphan_images.delete()