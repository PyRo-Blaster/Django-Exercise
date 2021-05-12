from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from jobs.models import Job
from jobs.models import Job_Types, Job_Cities

#通过joblist函数加载joblist.html页面
def joblist(request):
    #加载Job类的objects,按job_type排序
    job_list = Job.objects.order_by('job_type')
    template = loader.get_template('joblist.html')
    context = {'job_list': job_list}

    for job in job_list:
        #注意引用列表元素的第二个元祖元素[1],否则会出冒号
        job.city_name = Job_Cities[job.job_city][1]
        job.job_type = Job_Types[job.job_type][1]

    return HttpResponse(template.render(context))

#加载job.html页面
def detail(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
        job.city_name = Job_Cities[job.job_city][1]
    except Job.DoesNotExist:
        raise Http404("Job Does Not Exist")

    return render(request, 'job.html', {'job': job})
