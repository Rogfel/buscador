from django.db import models

class Article(models.Model):
    STATUS_TYPES = (
        (0 , 'Pending'),
        (1 , 'Reviewed'),
        (2 , 'Published'),
        (3 , 'Expired')
    )
    name = models.CharField(max_length=100)
    value = models.TextField (max_length=500)
    status = models.PositiveSmallIntegerField (choices=STATUS_TYPES, 
                                        default= STATUS_TYPES[0])

