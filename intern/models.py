from django.db import models


class demo(models.Model):
    Name = models.CharField(max_length=100,default="")
    Email = models.CharField(max_length=100,default="")
    PhoneNumber = models.CharField(max_length=11,default="")
    Message= models.CharField(max_length=100,default="")
    class Meta:
        db_table="user_query"
        print("done")
