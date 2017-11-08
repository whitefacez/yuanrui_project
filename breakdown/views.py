from django.shortcuts import render
from breakdown.models import *
from django.http import HttpResponseRedirect
from breakdown.forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

#class breakdownlogin(TemplateView):
 #   template_name= 'info.html'

#故障录入
@login_required
def addbreakdownlogin(request):
        if request.method == 'POST':
            form = BreakdownloginForm(request.POST)
            if form.is_valid():
                Breakdownlogin = form.save()
                return HttpResponseRedirect('loglist')
        else:
            form = BreakdownloginForm()
        return render(request,'BDlogin.html', {'form': form})

def addbreakdownResult(request):
        if request.method == 'POST':
            formBDResult = BreakdownResultForm(request.POST)
            if formBDResult.is_valid():
                BreakdownResult = formBDResult.save()
                return HttpResponseRedirect('BDResult.html')
        else:
            formBDResult = BreakdownResultForm()
        return render(request,'BDResult.html', {'formBDResult':formBDResult})

@login_required
def showbreakdownlogin_list(request):
    login_list = Breakdownlogin.objects.all()
    return render(request, 'LoginList.html',{'login_list': login_list})

def updatebreakdownlogin_list(request,pk):
    ChangedateForm = Breakdownlogin.objects.get(LoginNo = pk) 
    ChangedateForm.Result =  request.POST.get('Result')

    ChangedateForm.save()  
    return HttpResponseRedirect('/breakdown/loglist')  

'''
       if request.method == 'POST':
            ChangedateForm = BreakdownloginForm(request.POST)
            if ChangedateForm.is_valid():
                Breakdownlogin = ChangedateForm.save()
                return HttpResponseRedirect('loglist')
        else:
            ChangedateForm = BreakdownloginForm()
        return render(request,'updatelist.html', {'ChangedataForm': ChangedateForm}) '''


def updatebreakdownlogin(request, pk):  
    ChangedateForm = Breakdownlogin.objects.filter(LoginNo = pk)  
    return render(request, 'updatelist.html', {'ChangedateForm' : ChangedateForm})  

'''   if request.method == 'POST':
        ChangedateForm = Breakdownlogin(request.POST)
        if ChangedateForm.is_valid():
            ChangedateForm = ChangedateForm.save()
            return HttpResponseRedirect('updatelist.html')
    else:
        ChangedateForm =  Breakdownlogin.objects.filter(LoginNo = pk)
    return render(request,'updatelist.html', {'ChangedateForm':ChangedateForm})

        '''
def delectbreakdownlist(request, pk):
    delectdateForm = Breakdownlogin.objects.get(LoginNo = pk)
    delectdateForm.delete()
    return HttpResponseRedirect('/breakdown/loglist') 