import fitz  # PyMuPDF
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookUploadForm
from .models import Book
from django.conf import settings
import os
from django.views.decorators.http import require_POST

def upload_book(request):
    if request.method == 'POST':
        form = BookUploadForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()

            # Proses konversi PDF ke cover image (halaman pertama saja)
            pdf_path = book.file.path
            doc = fitz.open(pdf_path)
            output_dir = os.path.join(settings.MEDIA_ROOT, 'books/images/', str(book.id))
            os.makedirs(output_dir, exist_ok=True)

            # Proses hanya halaman pertama
            if len(doc) > 0:
                page = doc.load_page(0)  # Halaman pertama
                pix = page.get_pixmap()
                cover_image_path = os.path.join(output_dir, "cover.png")
                pix.save(cover_image_path)

                # Update cover_image di model
                book.cover_image = f"books/images/{book.id}/cover.png"
                book.save()

            return redirect('home')
    else:
        form = BookUploadForm()

    return render(request, 'upload_book.html', {'form': form})




def home_view(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookUploadForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = BookUploadForm(instance=book)
    return render(request, 'edit_book.html', {'form': form, 'book': book})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    return render(request, 'confirm_delete.html', {'book': book})