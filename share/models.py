from django.db import models

# Create your models here.

class BaseInfo(models.Model):
    date = models.CharField("日期",max_length=64)
    code = models.CharField("代码",max_length=64)
    name = models.CharField("名称",max_length=255)
    url = models.CharField("url",max_length=255)
    present_price = models.CharField("现价",max_length=64,null=True)
    range = models.CharField("涨跌幅",max_length=64,null=True)
    price_range = models.CharField("涨跌",max_length=64,null=True)
    rise_speed = models.CharField("涨速",max_length=64,null=True)
    change_hands = models.CharField("换手",max_length=64,null=True)
    volume_ratio = models.CharField("量比",max_length=64,null=True)
    amplitude = models.CharField("振幅",max_length=64,null=True)
    turnover = models.CharField("成交额",max_length=64,null=True)
    floating_stock = models.CharField("流通股",max_length=64,null=True)
    circulation_market_value = models.CharField("流通市值",max_length=64,null=True)
    pe_ratio = models.CharField("市盈率",max_length=64,null=True)
    create_time = models.DateTimeField("创建时间",auto_now_add=True)
    update_time = models.DateTimeField("更新时间",auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "基本信息"
        verbose_name_plural = "基本信息"

