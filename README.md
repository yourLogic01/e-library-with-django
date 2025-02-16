# E-Library dengan Django

E-Library adalah aplikasi perpustakaan digital yang memungkinkan pengguna untuk mengunggah, melihat, dan membaca buku dalam format PDF. Aplikasi ini menggunakan **Django** sebagai backend dan **Bootstrap** untuk styling.

## Persyaratan:

- Python 3.x
- Django 4.x
- PyMuPDF
- Bootstrap 5.x
- Virtual Environment (direkomendasikan)

---

## Instalasi:

1. **Clone Repository:**

   ```bash
   git https://github.com/yourLogic01/e-library-with-django
   cd e-library
   ```

2. **Buat Virtual Environment dan Aktifkan:**

   ```bash
   python -m venv env
   source env/bin/activate   # Untuk MacOS/Linux
   .\env\Scripts\activate    # Untuk Windows
   ```

3. **Install Dependencies:**

   ```bash
   ex : pip install django pyMuPdf dll
   ```

4. **Migrate Database:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Jalankan Server:**
   ```bash
   python manage.py runserver
   ```
   Buka di browser: [http://localhost:8000](http://localhost:8000)

---

## Konfigurasi Lingkungan:

Buat file **.env** di root proyek dengan isi sebagai berikut:

```
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost, 127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

---

## Penggunaan:

- **Registrasi** untuk membuat akun baru.
- **Login** untuk masuk ke sistem.
- **Upload Buku** dalam format PDF, sistem akan otomatis mengonversi PDF menjadi gambar.
- **Lihat Detail Buku** untuk membaca preview dalam bentuk gambar.
- **Edit atau Hapus Buku** yang sudah diunggah.
- **Logout** untuk keluar dari akun.

## Teknologi yang Digunakan:

- **Backend:** Django
- **Frontend:** Bootstrap 5
- **Database:** SQLite (default)
- **PDF Conversion:** PyMuPDF

---

## Kontributor:

- Nama Anda [GitHub](https://github.com/yourLogic01)

---

## Catatan:

- Pastikan **virtual environment** diaktifkan sebelum menjalankan server.
- Gunakan **Python 3.8 atau lebih baru** untuk kompatibilitas.
