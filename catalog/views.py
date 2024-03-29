from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.

def index(request):
    """ View function for home page of site."""

    #Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    #Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    #The 'all()' is implied by default.
    num_authors = Author.objects.count()

    brain_books=Book.objects.filter(title__icontains='brain').count()
    num_kids_genre=Book.objects.filter(genre__name__icontains='children').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'brain_books': brain_books,
        'num_kids_genre': num_kids_genre,
    }

    #Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context = context)


class BookListView(generic.ListView):
    model = Book
    paginate_by=5

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author
