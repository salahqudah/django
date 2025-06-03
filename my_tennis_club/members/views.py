from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Member
from datetime import datetime,date
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
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
        
        return Response({"message": "You posted:", "data": request.data})
class HelloWorldAPIView(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"})

    def post(self, request):
        return Response({"message": "You posted", "data": request.data}, 
                        status=status.HTTP_201_CREATED)
  
class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

  

