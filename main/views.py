from django.shortcuts import render
from placement.models import Company, Saved_Company, Salary, New_Job, Saved_Job
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from datetime import datetime
from django.http import HttpResponse


# Create your views here.
@login_required(login_url='/user/login')
def home(request):
    saved_job_user = Saved_Job.objects.filter(user_id = request.user)
    context = {
        "home": 'active',
        'Company' : Company.objects.all(),
		'User_Company' : Saved_Company.objects.all(),
        'jobs':New_Job.objects.all(),
		'Salary' : Salary.objects.all(),
        'Saved_jobs' : [i.job_id.id for i in saved_job_user],
        'applied_jobs' : [(i.job_id.id) if(i.applied) else -1 for i in saved_job_user],
        'rejected_jobs' : [(i.job_id.id) if(i.rejected) else -1 for i in saved_job_user],
        'reffered_jobs' : [(i.job_id.id) if(i.reffred) else -1 for i in saved_job_user],
        'selected_jobs' : [(i.job_id.id) if(i.selected) else -1 for i in saved_job_user],
        "totalSJ" : len(saved_job_user),
        "chk" : "True"
    }
    
    context['totalaj'] =  sum(map(lambda x : x>0 , context['applied_jobs']))
    context['totalref'] = sum(map(lambda x : x>0 , context['reffered_jobs']))
    context['totalrj'] =  sum(map(lambda x : x>0 , context['rejected_jobs']))
    context['totalselt'] =  sum(map(lambda x : x>0 , context['selected_jobs']))
    print(context['totalaj'] )
    return render(request, 'main/home.html',context)


@login_required(login_url='/user/login')
def profile(request):


    return render(request, 'main/profile.html')


def save_job(request):
    if request.method =="GET":
        jobid = request.GET['jobid']
        user = request.user
        ap = True if (request.GET['applied'] == 'true') else False 
        ref =  True if (request.GET['reffered'] == 'true') else False
        rj = True if (request.GET['rejected'] == 'true') else False 
        selt = True if (request.GET['selected'] == 'true') else False
        print(ap,ref,rj,selt)
        print(True)
        
        sj = Saved_Job.objects.filter(user_id = user, job_id_id = jobid)
        if(sj.exists()):
            sj.delete()
            print("unsave")
            status = 'unsave'
        else:
            Saved_Job(user_id =user,job_id_id = jobid, applied=ap, reffred=ref, rejected=rj, selected=selt).save()
            print("save")
            status = 'save'
        total = Saved_Job.objects.filter(user_id = user)


        return JsonResponse({'status':status, 'total': len(total)})

def changeName(request):
    if(request.method == "POST"):
        nfm = request.POST["nfName"]
        nlm = request.POST["nlName"]
        usr = User.objects.get(pk = request.user.id)
        usr.first_name = nfm
        usr.last_name = nlm
        usr.save()
        return JsonResponse({'fname':nfm, 'lname':nlm})



