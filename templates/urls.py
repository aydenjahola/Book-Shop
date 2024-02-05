from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.search, name='search'),
    path('books/', views.view_all_books, name="all_books"),
    path('books/<int:bookid>/', views.view_single_book, name='single_book'),
    path('books/year/<int:year>/', views.view_books_by_year, name='books_by_year'),
    path('books/category/<str:category>/',
         views.view_books_by_catergory, name='books_by_category'),
    path('books/category/<str:category>/year/<int:year>/',
         views.view_books_by_year_and_category, name='books_by_year_and_category'),
    path('books/authors/', views.view_all_authors, name='all_authors'),
    path('authors/<int:authorid>/', views.view_single_author, name='single_author'),
    path('books/categories/', views.view_all_categories, name='all_categories'),
    path('books/years/', views.view_all_years, name='all_years')
]
