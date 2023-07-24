from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookTableView.as_view()),
    path('', views.bookhome),
    path('booklist/', views.showbooks),
    path('booktable/', views.showbooksrawtable),
]