from django.db import models


class UserOrderModerateTitle(models.Model):
    orderId = models.CharField('Id', max_length=3)
    orderTitle = models.CharField('Название закупки', max_length=50)
    order_date = models.DateTimeField

class UserOrderModerateDescription(models.Model):
    orderDescription = models.TextField('Потроха закупки')
