from django.db import models
from django.forms import ModelForm,Select
from django.utils.translation import ugettext_lazy as _

#
def get_object(modelname,firstkey):
    r = []
    r = modelname.objects.values_list('id', firstkey)
      #  for obj in modelname.objects.all():
      #      r = r + [(obj.id, obj.values(firstkey))]
    return r


# Create your models here.

#-------------------------------------------------------------------
#故障级别
class BreakdownLevel(models.Model): 
    BreakdownName = models.CharField(max_length = 20)
    LRemarks = models.CharField(max_length = 200)


#------------------------------------------------------------------------#
#故障类型
class BreakdownType(models.Model):
    BDTName = models.CharField(max_length = 20)
    BDTLevel = models.CharField(max_length = 20)
    

#------------------------------------------------------------------------#
#故障处理
class BreakdownResult(models.Model):
    BDRName = models.CharField(max_length = 20)
    BDRRemarks = models.CharField(max_length = 200)

class BreakdownResultForm(ModelForm):
    class Meta:
        model = BreakdownResult
        fields = '__all__'
        labels = {
            'BDRName':_('处理结果'),
            'BDRRemarks':_('备注'),
        }


#------------------------------------------------------

#故障录入
class Breakdownlogin(models.Model):
    LoginNo = models.CharField(max_length = 20,primary_key = True)
    Result = models.CharField(max_length = 20)
    BreakdownLevel = models.CharField(max_length = 20 )
    BreakdownType = models.CharField(max_length = 20 )
    Line = models.CharField(max_length = 20 )
    Site = models.CharField(max_length = 20 )
    Coach = models.CharField(max_length = 10 )
    Position = models.CharField(max_length = 20 )
    BreakdownCount = models.IntegerField()
    Keyboard = models.CharField(max_length = 20 )
    Processor = models.CharField(max_length = 20 )
    BreakdownDate = models.DateField()
    LoginRemark = models.CharField(max_length = 200,blank=True)    


class BreakdownloginForm(ModelForm):
    class Meta:
        model = Breakdownlogin
        fields = '__all__'
        labels={
            'LoginNo' :_('报障编码'),
            'Result' :_('处理结果'),
            'BreakdownLevel':_('故障级别'),
            'BreakdownType':_('故障类型'),
            'Line':_('所属线路'),
            'Site':_('所属站点'),
            'Coach':_('车厢编号'),
            'Position' :_('位置'),
            'BreakdownCount' :_('故障数量'),
            'Keyboard':_('录入员'),
            'Processor' :_('处理人'),
            'BreakdownDate':_('报修时间'),
            'LoginRemark':_('处理情况'),
        }
  #      widgets = {
   #         'BreakdownLevel' : Select(choices = get_object(BreakdownLevel,"BreakdownName")),
   #         'Result'  : Select(choices = get_object(BreakdownResult,"BDRName")),
            
  #      }

 