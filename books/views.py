from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import render
from django_tables2 import SingleTableView, tables, SingleTableMixin
from django_filters.views import FilterView
from django_filters import FilterSet

from django.core.paginator import Paginator
from books.models import Book

SingleTableView.table_pagination = {"per_page": 6}


# def books(request):
#     template = loader.get_template('show_book_list.html')
#     return HttpResponse(template.render())
#
#     user_list = User.objects.all()
#     page = request.GET.get('page', 1)
#
#     paginator = Paginator(user_list, 10)
#     try:
#         users = paginator.page(page)
#     except PageNotAnInteger:
#         users = paginator.page(1)
#     except EmptyPage:
#         users = paginator.page(paginator.num_pages)
#
#     return render(request, 'show_book_list.html', {'users': books})
def bookhome(req):
    template = loader.get_template('header_test.html')
    return HttpResponse(template.render())
    #return HttpResponse("Hello world!")

def showbooks(req):
    query = req.GET.get('q')
    if query:
        table = BookTable(Book.objects.filter(Q(name__icontains=query))[:100])
        table.paginate(page=req.GET.get("page", 1), per_page=6)
        return render(req, "show_book_test.html", {"book_table":
                                                       table, "qq": query
                                                   })
    else:
        table = BookTable(Book.objects.all()[:100])
        table.paginate(page=req.GET.get("page", 1), per_page=6)
        return render(req, "show_book_test.html", {"book_table":
                                                       table, "qq": ""
                                                   })
    #filter = BookFilter(request.GET, queryset=Product.objects.all())

    # return render(req, "show_book_test.html", {"table":
    #     table, "qq" : query
    # })

def showBooksRawTable(req):

    query = req.GET.get('q')
    if query is None:
        books = Book.objects.all()[:100]
        query = ''
    else:
        books = Book.objects.filter(Q(name__icontains=query))[:100]
    field = Book._meta.get_fields()
    return render(req, "show_book_table_raw.html", { "qq": query, "books": books, "book_fields":field})

def showPapersRawTable(req):

    query = req.GET.get('q')
    if query is None:
        books = Book.objects.all()[:100]
        query = ''
    else:
        books = Book.objects.filter(Q(name__icontains=query))[:100]
    field = Book._meta.get_fields()
    return render(req, "show_paper_table_raw.html", { "qq": query, "books": books, "book_fields":field})

def getPaper(req, paper_id):
    #iidd = req.GET.get('paper_id')
    return JsonResponse({"paper_id":paper_id,
                         #"paper_path":"D:\Sahed_works\Account Opening\From_Mamun_Sir.jpg"})
                        #"paper_path":"C:\\Users\Eblict\Desktop\A15_Presentation.pdf"})
                         "paper_path": "https://www.africau.edu/images/default/sample.pdf"})

def showAPaper(req, paper_id):
    paper = Book.objects.get(id=paper_id)
    #return JsonResponse({"paper_id": req})
    return render(req, "show_a_paper.html", {"paper": paper,
                                             "paper_path": "https://www.africau.edu/images/default/sample.pdf"})



class BookTable(tables.Table):
    class Meta:
        attrs = {"class": "mytable"}
        model = Book
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "writer", "link", "price", "rating")

class BookTableView(SingleTableView):
    model = Book
    table_class = BookTable
    template_name = "show_book_test.html"
    #template_name = "topnavbar_test.html"

    def get_queryset(self):  # new
    #def do_query(self):  # new
        query = self.request.GET.get('q')
        if query is None:
            return Book.objects.all()[:100]
        return Book.objects.filter(
            Q(name__icontains=query)
        )[:100]


class BookFilter(FilterSet):
    class Meta:
        model = Book
        fields = {"name": ["exact", "contains"], "writer": ["contains"], "rating": ["contains"], "price": ["contains"]}


class FilteredPersonListView(SingleTableMixin, FilterView):
    table_class = BookTable
    model = Book
    template_name = "show_book_test.html"

    filterset_class = BookFilter

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(name__icontains=query)
        )




