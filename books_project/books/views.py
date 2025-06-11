from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from .serializers import BookSerializer

from .models import Books

# Create your views here.

class BooksListCreateView(APIView):

    serializer_class = BookSerializer

    def get(self,request,*args,**kwargs):

        books = Books.objects.all()

        book_serializer = self.serializer_class(books,many=True)

        data = {'books':book_serializer.data}

        return Response(data=data,status=200)
    
    def post(self, request,*args,**kwargs):

        book_serializer = self.serializer_class(data=request.data)

        if book_serializer.is_valid():

            book_serializer.save()

            return Response(data={'msg':'This is the create view'},status=200)
        
        return Response(data=book_serializer.errors,status=400) 

        # data = {'msg':'This is the create view'}

        return Response(data=data,status=200)
    
class BooksRetrieveUpdateDestroyView(APIView):

    def get(self, request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        data = {'uuid': uuid,'arg':'This is Retrieve view'}

        return Response(data=data,status=200)
    
    def put(self, request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        data = {'uuid': uuid,'arg':'This is Update view'}

        return Response(data=data,status=200)
    
    def delete(self, request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        data = {'uuid': uuid,'arg':'This is Delete view'}

        return Response(data=data,status=200)