from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Member
from datetime import datetime,date
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Item,Book
from .serializers import ItemSerializer, BookSerializer
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

@api_view(['GET', 'POST'])
def book_fbv(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookCBV(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

from rest_framework import generics, mixins

class BookMixinView(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

from django.shortcuts import render

def render_fbv_form(request):
    return render(request, 'base_template.html', {'title': 'FBV Form'})

def render_cbv_form(request):
    return render(request, 'base_template.html', {'title': 'CBV Form'})

def render_mixin_form(request):
    return render(request, 'base_template.html', {'title': 'Mixin Form'})
