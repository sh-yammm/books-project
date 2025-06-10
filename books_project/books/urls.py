from django.urls import path

from . import views

urlpatterns = [

    path('books/',views.BooksListCreateView.as_view()),

    path('books/<str:uuid>/',views.BooksRetrieveUpdateDestroyView.as_view()),

]