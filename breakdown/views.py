from django.shortcuts import render
from breakdown.models import Breakdownlogin,BreakdownLevel,BreakdownResult,BreakdownloginForm,BreakdownResultForm
from django.http import HttpResponseRedirect

# Create your views here.

#class breakdownlogin(TemplateView):
 #   template_name= 'info.html'

#故障录入
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

def showbreakdownlogin_list(request):
    login_list = Breakdownlogin.objects.all()
    return render(request, 'LoginList.html',{'login_list': login_list})

def updatebreakdownlogin_list(request,pk):
    changedate =  Breakdownlogin.objects.get(id = pk)
    if request.POST.has_key('Result'):
        changedate.request = request.POST['Result']
    changedate.save()
    return HttpResponseRedirect('/loglist/' )

        