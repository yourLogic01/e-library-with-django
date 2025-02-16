from django import forms
from .models import Book

class BookUploadForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['file', 'title', 'description', 'author', 'publication_year', 'genre']
        widgets = {
            'file': forms.ClearableFileInput(attrs={
                'class': 'form-control', 
                'accept': 'application/pdf',
                'aria-describedby': 'fileHelp'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Masukkan judul buku'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3,
                'placeholder': 'Deskripsi singkat buku'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nama penulis'
            }),
            'publication_year': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Tahun terbit'
            }),
            'genre': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Genre buku'
            }),
        }

    def clean_file(self):
        file = self.cleaned_data['file']
        if not file.name.endswith('.pdf'):
            raise forms.ValidationError("Hanya file PDF yang diperbolehkan.")
        return file
