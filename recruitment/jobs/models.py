from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

Job_Types = [
    (0,'技术类'),
    (1,'产品类'),
    (2,'运营类'),
    (3,'设计类')
]
Job_Cities = [
    (0,'北京'),
    (1,'上海'),
    (2,'深圳')
]
# Create your models here.
class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False,choices=Job_Types,verbose_name='岗位类型')
    job_name = models.CharField(max_length=250,blank=False,verbose_name='岗位名称')
    job_city = models.SmallIntegerField(blank=False,choices=Job_Cities,verbose_name='工作地点')
    job_responsibiltiy = models.TextField(max_length=250,verbose_name='岗位职责')
    job_requirement = models.TextField(max_length=1024,blank=False,verbose_name='岗位需求')
    creator = models.ForeignKey(User,verbose_name='创建人',null=True,on_delete=models.SET_NULL)
    create_time = models.DateTimeField(verbose_name='创建日期',default=datetime.now)
    modified_time = models.DateTimeField(verbose_name='修改日期',default=datetime.now)
