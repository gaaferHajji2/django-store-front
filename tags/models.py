from django.db import models

from django.contrib.contenttypes.models import ContentType

from django.contrib.contenttypes.fields import GenericForeignKey

class Tag(models.Model):
    label = models.CharField(max_length=255)

    def __str__(self): 
        return self.label

class TaggedItemManager(models.Manager):
    def get_tags_for(self, obj_type, obj_value):
        content_type = ContentType.objects.get_for_model(obj_type)

        # Here We Use select_related To Avoid The Problems Of 
        # Loading Many Tags
        return TaggedItem.objects\
            .select_related('tag')\
            .filter(
                content_type = content_type,
                object_id=obj_value
        )

class TaggedItem(models.Model):

    objects = TaggedItemManager()

    tag = models.ForeignKey(to=Tag, on_delete=models.CASCADE)
    
    content_type = models.ForeignKey(to=ContentType, on_delete=models.CASCADE)

    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey()

    def __str__(self):
        return self.content_type.__str__() + ' - ' + self.tag.__str__()