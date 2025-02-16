from django.db import models
import os
from django.conf import settings

class Book(models.Model):
    file = models.FileField(upload_to='books/pdf/', help_text="Upload file PDF saja.")
    cover_image = models.ImageField(upload_to='books/images/', blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def delete(self, *args, **kwargs):
        # Hapus file dan cover image dari sistem penyimpanan
        if self.file:
            file_path = os.path.join(settings.MEDIA_ROOT, self.file.name)
            if os.path.exists(file_path):
                os.remove(file_path)
        
        if self.cover_image:
            image_path = os.path.join(settings.MEDIA_ROOT, self.cover_image.name)
            if os.path.exists(image_path):
                os.remove(image_path)
        
        # Hapus folder kosong setelah file dihapus
        output_dir = os.path.join(settings.MEDIA_ROOT, 'books/images/', str(self.id))
        if os.path.exists(output_dir) and not os.listdir(output_dir):
            os.rmdir(output_dir)

        # Hapus objek dari database
        super().delete(*args, **kwargs)