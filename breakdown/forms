from django import forms
from breakdown.models import *
def get_object(modelname,firstkey):
    r = []
    r = modelname.objects.values_list('id', firstkey)
      #  for obj in modelname.objects.all():
      #      r = r + [(obj.id, obj.values(firstkey))]
    return r

class BreakdownloginForm(forms.Form):
    LoginNo = forms.CharField(max_length = 20,label = '报障编码')

    Result = forms.CharField(max_length = 20,label = '处理结果',
    widget = forms.Select(choices = get_object(BreakdownResult,"BDRName")))

    BreakdownLevel = forms.CharField(max_length = 20, label = '故障级别',
    widget = forms.Select(choices = get_object(BreakdownLevel,"BreakdownName")))

    BreakdownType = forms.CharField(max_length = 20, label = '故障类型')

    Line = forms.CharField(max_length = 20, label = '所属线路')

    Site = forms.CharField(max_length = 20, label = '所属站点')

    Coach = forms.CharField(max_length = 10, label = '车厢编号' )

    Position = forms.CharField(max_length = 20,label ='位置')

    BreakdownCount = forms.IntegerField(label = '故障数量')

    Keyboard = forms.CharField(max_length = 20, label = '录入员' )

    Processor = forms.CharField(max_length = 20, label = '处理人' )

    BreakdownDate = forms.DateField(label = '报修时间')
    
    LoginRemark = forms.CharField(max_length = 200,label = '备注')    