from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookTableView.as_view()),
    path('', views.bookhome),
    path('booklist/', views.showbooks),
    path('booktable/', views.showBooksRawTable),
    path('papertable/', views.showPapersRawTable),
    path('papertable/paper/<str:paper_id>',views.getPaper)
]