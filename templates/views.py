from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404


def index(request):
    featured_books = Book.objects.filter(is_featured=True)
    return render(request, 'index.html', {'featured_books': featured_books})


def search(request):
    query = request.GET.get('q')
    if query:
        results = Book.objects.filter(
            models.Q(title__icontains=query) |
            models.Q(author__icontains=query) |
            models.Q(category__icontains=query) |
            models.Q(year__icontains=query)
        )
    else:
        results = []

    return render(request, 'search_results.html', {'results': results, 'query': query})


def view_all_books(request):
    all_books = Book.objects.all()
    return render(request, 'all_books.html', {'books': all_books})


def view_single_book(request, bookid):
    single_book = get_object_or_404(Book, id=bookid)
    return render(request, 'single_book.html', {'book': single_book})


def view_books_by_year(request, year):
    books_by_year = get_list_or_404(Book, year=year)
    return render(request, 'books_by_year.html', {'books': books_by_year, 'year': year})


def view_books_by_catergory(request, category):
    books_by_category = get_list_or_404(Book, category=category)
    return render(request, 'books_by_category.html', {'books': books_by_category, 'category': category})


def view_books_by_year_and_category(request, category, year):
    books_by_year_and_category = get_list_or_404(
        Book, category=category, year=year)
    return render(request, 'books_by_year_and_category.html', {'books': books_by_year_and_category, 'category': category, 'year': year})


def view_all_authors(request):
    all_authors = Book.objects.values('author').distinct()
    books_by_author = []
    for author in all_authors:
        books = Book.objects.filter(author=author['author'])
        books_by_author.append({'author': author['author'], 'books': books})
    return render(request, 'all_authors.html', {'authors': all_authors, 'books_by_author': books_by_author})


def view_all_categories(request):
    all_categories = Book.objects.values('category').distinct()
    books_by_category = []
    for category in all_categories:
        books = Book.objects.filter(category=category['category'])
        books_by_category.append(
            {'category': category['category'], 'books': books})
    return render(request, 'all_categories.html', {'categories': all_categories, 'books_by_category': books_by_category})


def view_all_years(request):
    all_years = Book.objects.values('year').distinct()
    books_by_year = []
    for year in all_years:
        books = Book.objects.filter(year=year['year'])
        books_by_year.append(
            {'year': year['year'], 'books': books})
    return render(request, 'all_years.html', {'years': all_years, 'books_by_year': books_by_year})
