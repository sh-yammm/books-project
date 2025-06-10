from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

# Create your views here.

class BooksListCreateView(APIView):

    def get(self,request,*args,**kwargs):

        data = {'msg':'This is the list view'}

        return Response(data=data,status=200)
    
    def post(self, request,*args,**kwargs):

        data = {'msg':'This is the create view'}

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