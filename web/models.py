from django.db import models

# Create your models here.
class Customer(models.Model):

    name = models.CharField(max_length=32,verbose_name='客户姓名')
    age = models.IntegerField(verbose_name='客户年龄')
    tel = models.CharField(verbose_name='客户电话',max_length=11)
    email = models.EmailField(verbose_name='客户邮箱')

    def __str__(self):
        return self.name

class Payment(models.Model):

    money = models.IntegerField(verbose_name='支付金额')
    time = models.DateTimeField(verbose_name='支付时间',auto_now_add=True)

    customer = models.ForeignKey(verbose_name='支付客户',to='Customer',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.money)