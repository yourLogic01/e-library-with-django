from django.urls import path
from .views import home_view, upload_book, book_detail, edit_book, delete_book

urlpatterns = [
    path('', home_view, name='home'),
    path('upload/', upload_book, name='upload_book'),
    path('book/<int:book_id>/', book_detail, name='book_detail'),  # Ganti id -> book_id
    path('book/<int:book_id>/edit/', edit_book, name='edit_book'),
    path('book/<int:book_id>/delete/', delete_book, name='delete_book'),
]

