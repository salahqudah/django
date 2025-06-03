from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Member
from datetime import datetime,date

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  mydata=Member.objects.filter(firstname='salah').values()|Member.objects.filter(firstname='Tobias').values()
  template = loader.get_template('template.html')
  context =  {
      'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
def orderbyfirst(request):
  mydata= Member.objects.all().order_by('firstname').values()
  template = loader.get_template('template.html')
  context = {
      'mymembers': mydata,
  }
  return HttpResponse(template.render(context,request))
def descendingby(request):
  mydata=Member.objects.all().order_by('-firstname').values()
  template= loader.get_template('template.html')
  context = {
    'mymembers':mydata,
  }
  return HttpResponse(template.render(context,request))

  

  

