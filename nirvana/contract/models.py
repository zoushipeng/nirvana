#!/usr/bin/env python
# coding=utf8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Sales(models.Model):
    name = models.CharField(u"销售姓名",max_length=128)
    telephone = models.CharField(u"联系方式",max_length=128)


class Company(models.Model):
    name = models.CharField(u"公司名称",max_length=128)
    address = models.CharField(u"公司地址",max_length=128)
    bank_number = models.CharField(u"公司账户",max_length=128)


class Contract(models.Model):
    name = models.CharField(u"合同名称",max_length=128)
    start_time = models.DateField(u"合同开始时间")
    end_time = models.DateField(u"合同结束时间")
    stop_time = models.DateField(u"合同终止时间")
    sales = models.ForeignKey(Sales,related_name="contracts")
    company = models.ForeignKey(Company,related_name="contracts")
    customer = models.CharField(u"用户",max_length=128)
    telephone = models.CharField(u"联系方式",max_length=128)
    remark = models.CharField(u"备注",max_length=256)
