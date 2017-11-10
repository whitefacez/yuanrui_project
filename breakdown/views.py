from django.shortcuts import render
from breakdown.models import Breakdownlogin,BreakdownloginForm,BreakdownLevel,BreakdownResult,BreakdownResultForm,BreakdownType
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
#from breakdown.forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.

#class breakdownlogin(TemplateView):
 #   template_name= 'info.html'

#故障录入
#@login_required
def addbreakdownlogin(request):
        if request.method == 'POST':
            form = BreakdownloginForm(request.POST or None)
            if form.is_valid():
                Breakdownlogin = form.save()
                return HttpResponseRedirect('loglist')
        else:
            form = BreakdownloginForm()
        return render(request, 'BDlogin.html' , {'form': form} )

def addbreakdownResult(request):
        if request.method == 'POST':
            formBDResult = BreakdownResultForm(request.POST)
            if formBDResult.is_valid():
                BreakdownResult = formBDResult.save()
                return HttpResponseRedirect('BDResult.html')
        else:
            formBDResult = BreakdownResultForm()
        return render(request,'BDResult.html', {'formBDResult':formBDResult})

#@login_required
def showbreakdownlogin_list(request):
    if request.method == 'GET':
        DateStart = request.GET['DateStart']
        DateEnd = request.GET["DateEnd"]
        login_list = Breakdownlogin.objects.filter(BreakdownDate__range = (DateStart,DateEnd))
    else:
        login_list = Breakdownlogin.objects.all()
    return render(request, 'LoginList.html',{'login_list': login_list})

'''
def showbreakdownlogin_list_date(request):
    DateStart = request.Post.get('DateStart')
    DateEnd = request.Post.get("DateEnd")
    login_list = Breakdownlogin.objects.filter(BreakdownDate__range = (DateStart,DateEnd))
    return render(request, 'LoginList.html',{'login_list': login_list})
'''


def updatebreakdownlogin_list(request,pk):
    ChangedateForm = Breakdownlogin.objects.get(LoginNo = pk) 
    if request.method == 'POST':
        ChangedateForm.Result =  request.POST.get('Result')
        ChangedateForm.BreakdownLevel =  request.POST.get('BreakdownLevel')
        ChangedateForm.BreakdownType =  request.POST.get('BreakdownType')
        ChangedateForm.Line =  request.POST.get('Line')
        ChangedateForm.Site =  request.POST.get('Site')
        ChangedateForm.Coach =  request.POST.get('Coach')
        ChangedateForm.Position =  request.POST.get('Position')
        ChangedateForm.BreakdownCount =  request.POST.get('BreakdownCount')
        ChangedateForm.Keyboard =  request.POST.get('Keyboard')
        ChangedateForm.Processor =  request.POST.get('Processor')
        ChangedateForm.BreakdownDate =  request.POST.get('BreakdownDate')
        ChangedateForm.LoginRemark =  request.POST.get('LoginRemark')
        ChangedateForm.save()
        return HttpResponseRedirect('/breakdown/loglist')
    else:
        pass
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
#    return render(request, 'updatelist.html', {'ChangedateForm' : ChangedateForm}) 
    ChangedateForm = Breakdownlogin.objects.filter(LoginNo = pk)  
    return render(request, 'updatelist.html', {'ChangedateForm' : ChangedateForm})  
'''
        if request.method == 'POST':
            form = BreakdownloginForm(request.POST)
            if form.full_clean(exclude =LoginNo ):
                form.save()
                return HttpResponseRedirect('breakdown/loglist')
        else:
            form = BreakdownloginForm()
            ChangedateForm = Breakdownlogin.objects.get(LoginNo=pk)
            form['LoginNo'].field.initial = ChangedateForm.LoginNo
            form['Result'].field.initial = ChangedateForm.Result
            form['BreakdownLevel'].field.initial = ChangedateForm.BreakdownLevel
            form['BreakdownType'].field.initial = ChangedateForm.BreakdownType
            form['Line'].field.initial = ChangedateForm.Line
            form['Site'].field.initial = ChangedateForm.Site
            form['Coach'].field.initial = ChangedateForm.Coach
            form['Position'].field.initial = ChangedateForm.Position
            form['BreakdownCount'].field.initial = ChangedateForm.BreakdownCount
            form['Keyboard'].field.initial = ChangedateForm.Keyboard
            form['Processor'].field.initial = ChangedateForm.Processor
            form['BreakdownDate'].field.initial = ChangedateForm.BreakdownDate
            form['LoginRemark'].field.initial = ChangedateForm.LoginRemark
        return render(request, 'updatelist.html' , {'form': form} )
'''
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