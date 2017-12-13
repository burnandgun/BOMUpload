# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.


class Part(models.Model):
    # Head = models.ForeignKey('self', verbose_name="父件", null=True, blank=True)
    # NO = models.IntegerField( verbose_name="件号", default = 0)
    ItemNO = models.CharField(max_length=30, verbose_name="物号", unique=True)
    Name = models.CharField(max_length=200, verbose_name="名称")
    EName = models.CharField(max_length=100, verbose_name="英文名称", null=True, blank=True)
    Matrial = models.CharField(max_length=50, verbose_name="材料", blank=True)
    Mass = models.FloatField(verbose_name="重量", null=True, blank=True)
    Unit = models.CharField(max_length=50, verbose_name="计量单位", null=True, blank=True)
    StandardNumber = models.CharField(max_length=50, verbose_name="标准号", blank=True, null=True)
    # Size = models.CharField(max_length=50, verbose_name="规格", blank=True, null=True)
    # ColorCode = models.CharField(max_length=50, verbose_name="颜色代码", blank=True, null=True)
    BelongedProNum = models.CharField(max_length=50, verbose_name="原属产品号", blank=True, null=True)
    Remark = models.CharField(max_length=100, verbose_name="备注", blank=True, null=True)
    DesignType = models.CharField(max_length=100, verbose_name="设计类型", blank=True, null=True)
    ManufactureRemark = models.CharField(max_length=100, verbose_name="制造备注", blank=True, null=True)
    isProduct = models.BooleanField(verbose_name="产品", default=False)
    isParts = models.BooleanField(verbose_name="部件", default=False)
    # Num = models.FloatField(verbose_name="数量", null=True, blank=True)
    Num = models.IntegerField(verbose_name="数量", null=True, blank=True)
    isFinish = models.BooleanField(verbose_name="完成", default=False)
    # DUser = models.ForeignKey(User, verbose_name="创建人", null=True, blank=True)
    Ratetime = models.DateField(verbose_name="考核时间", null=True, blank=True)
    # Token = models.CharField(max_length=64, verbose_name="Token", null=True, blank=True)
    # Department = models.ForeignKey(Department, verbose_name="部门", null=True, blank=True)

    def __unicode__(self):
        return u'%s' % (self.ItemNO.__str__() + ":" + self.Num.__str__())
    # self.ItemNO.__str__() + "#" +
    class Meta:
        verbose_name = "产品"
        verbose_name_plural = "产品汇总"
        #unique_together = ("ItemNO", "Department")


class Part_Con(models.Model):
    LNO = models.IntegerField(verbose_name="件号")
    Head = models.ForeignKey(Part, related_name='HeadBJ', verbose_name="主部件")
    Leef = models.ForeignKey(Part, related_name='LeefBJ', verbose_name="子部件")
    LeefNum = models.IntegerField(verbose_name="子部件数量")
   #  Token = models.ForeignKey(CloudLinkCode,  verbose_name="云联码", blank=True, null=True)
    isWatch = models.BooleanField(verbose_name="要求监视", default=False)

    def __unicode__(self):
        return u'%s' % (self.Head.__str__())

    class Meta:
        verbose_name = "产品关系"
        verbose_name_plural = "产品关系汇总"