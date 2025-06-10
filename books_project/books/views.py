from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

# Create your views here.

class BooksListCreateView(APIView):

    def get(self,request,*args,**kwargs):

        data = {'msg':'This is the list view'}

        return Response(data=data,status=200)