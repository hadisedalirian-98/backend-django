from django.db import models
from django.contrib.auth.models import User 


class GeneralModel(models.Model):
   
    create_at = models.DateTimeField("Created Time", auto_now_add=True)
    updated_at = models.DateTimeField("Updated Time", auto_now=True)
    
    # def __str__(self):
        # return f'{self.created_at}-{self.updated_at}-{self.created_by}'
    
    class Meta:
        abstract =True

    