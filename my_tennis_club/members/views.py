from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Member
from datetime import datetime,date
from rest_framework.decorators import api_view
from rest_framework.response import Response
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


def homepage(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'GET':
        return Response({"message": "Hello, world!"})
    elif request.method == 'POST':
        # echo back the posted data (JSON is parsed into request.data)
        return Response({"message": "You posted:", "data": request.data})

  

  

