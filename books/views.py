from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
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
        return render(req, "show_book_test.html", {"table":
                                                       table, "qq": query
                                                   })
    else:
        table = BookTable(Book.objects.all()[:100])
        table.paginate(page=req.GET.get("page", 1), per_page=6)
        return render(req, "show_book_test.html", {"table":
                                                       table, "qq": ""
                                                   })
    #filter = BookFilter(request.GET, queryset=Product.objects.all())

    # return render(req, "show_book_test.html", {"table":
    #     table, "qq" : query
    # })

class BookTable(tables.Table):
    class Meta:
        model = Book
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "writer", "link", "price", "rating")
        attrs = {"class": "mytable"}


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


