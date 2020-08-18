from django.db import models



class Values(models.Model):
    name = models.CharField(max_length=100)
    detail =  models.CharField(max_length=300)
    dateTime = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField()

    def __self__(self) -> str:
        return self.name

    def serialize(self):
        return{
            'dataTime': self.dateTime, 
            'name': self.name,
            'detail': self.detail,
        }