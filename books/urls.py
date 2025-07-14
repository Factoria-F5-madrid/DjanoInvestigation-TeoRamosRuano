from django.urls import path
from . import views

# URL patterns for the books app
urlpatterns = [
    path('', views.book_list, name='book_list'), # View for listing all books
    path('<int:book_id>/', views.book_detail, name='book_detail'), # View for book details
    path('create/', views.book_create, name='book_create'), # View to create a new book
    path('<int:book_id>/edit/', views.book_edit, name='book_edit'), # View to edit an existing book
    path('<int:book_id>/delete/', views.book_delete, name='book_delete'), # View to delete a book
]
