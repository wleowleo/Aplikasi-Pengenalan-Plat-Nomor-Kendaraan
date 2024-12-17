# **Pengenalan Plat Nomor Kendaraan**

Aplikasi ini digunakan untuk **mendeteksi** dan **membaca teks plat nomor kendaraan** secara otomatis dari gambar menggunakan teknik **pemrosesan citra** dan **Optical Character Recognition (OCR)**. Aplikasi ini memiliki antarmuka grafis (GUI) yang memudahkan pengguna dalam memilih gambar dan melihat hasil deteksi.

---

## **Fitur Aplikasi**

- **Pemilihan Gambar**: Pengguna dapat memilih gambar dari komputer melalui GUI.
- **Deteksi Plat Nomor**: Aplikasi akan mendeteksi area plat nomor kendaraan pada gambar.
- **Ekstraksi Teks**: Teks pada plat nomor akan dibaca secara otomatis menggunakan **Tesseract OCR**.
- **Tampilan Hasil**: Menampilkan gambar area plat nomor yang diproses dan teks hasil deteksi di GUI yang sama.

---

## **Teknologi yang Digunakan**

1. **Python**: Bahasa pemrograman utama.
2. **OpenCV**: Untuk pemrosesan citra (grayscale, edge detection, kontur, dll.).
3. **Pytesseract**: Untuk OCR (Optical Character Recognition).
4. **Tkinter**: Untuk membangun antarmuka grafis (GUI).
5. **Pillow (PIL)**: Untuk manipulasi gambar dalam GUI.

---

## **Instalasi**

Ikuti langkah-langkah di bawah ini untuk menjalankan aplikasi pada sistem lokal Anda.

### **1. Persyaratan Sistem**

- Python 3.x
- Paket berikut harus diinstal:
  - OpenCV
  - Pytesseract
  - Tkinter (sudah termasuk dalam Python standar)
  - Pillow

### **2. Instalasi Paket**

Buka terminal atau command prompt, lalu jalankan perintah berikut:

```bash
pip install opencv-python pytesseract pillow
```

### **3. Instalasi Tesseract OCR**

1. Unduh Tesseract OCR dari situs resminya: [Tesseract OCR Download](https://github.com/tesseract-ocr/tesseract).
2. Instal Tesseract di komputer Anda.
3. Tambahkan path Tesseract ke variabel lingkungan (PATH):
   - **Windows**: Biasanya di `C:\Program Files\Tesseract-OCR\tesseract.exe`.
   - **Linux/Mac**: Sesuaikan dengan path instalasi Anda.
4. Verifikasi instalasi dengan menjalankan perintah berikut di terminal:
   ```bash
   tesseract --version
   ```

---

## **Cara Menjalankan Aplikasi**

1. **Clone Repository atau Salin File**\
   Unduh atau clone kode program ke direktori lokal:

   ```bash
   git clone https://github.com/wleowleo/pengenalan-plat-nomor.git
   cd pengenalan-plat-nomor
   ```

2. **Jalankan Program**
   Eksekusi file Python menggunakan perintah:

   ```bash
   python main.py
   ```

3. **Gunakan Aplikasi**:

   - Aplikasi GUI akan muncul dengan halaman utama.
   - Klik tombol **"Choose Image"** untuk memilih gambar dari komputer Anda.
   - Aplikasi akan secara otomatis memproses gambar, mendeteksi plat nomor, dan menampilkan hasil:
     - **Gambar area plat nomor**.
     - **Teks hasil deteksi**.

---

## **Cara Kerja Aplikasi**

1. **Input Gambar**: Pengguna memilih gambar melalui GUI.
2. **Preprocessing Gambar**:
   - Konversi ke **grayscale** untuk menyederhanakan pemrosesan.
   - Menggunakan **Gaussian Blur** untuk mengurangi noise.
   - Deteksi tepi gambar menggunakan **Canny Edge Detection**.
3. **Deteksi Kontur**:
   - Aplikasi mencari kontur berbentuk **persegi panjang** sebagai kandidat plat nomor.
4. **Ekstraksi Plat Nomor**:
   - Area plat nomor dipotong dari gambar dan diubah ukurannya.
5. **OCR (Optical Character Recognition)**:
   - **Tesseract OCR** membaca teks dari area plat nomor.
6. **Output**:
   - Gambar area plat nomor dan teks hasil deteksi ditampilkan pada GUI.

---

## **Contoh Penggunaan**

1. **Input Gambar**:

2. **Hasil Deteksi**:

   - **Gambar Area Plat Nomor**:

   - **Teks Deteksi**:

     ```
     Detected Plate Text: B 1234 XYZ
     ```

---

## **Batasan Aplikasi**

- Gambar berkualitas rendah atau buram mungkin sulit diproses.
- Tidak mendukung deteksi plat nomor dari sudut yang terlalu miring.
- Aplikasi hanya membaca satu plat nomor dalam satu gambar.

---

## **Potensi Pengembangan**

- Menambahkan fitur deteksi banyak plat nomor dalam satu gambar.
- Mengintegrasikan dengan video streaming untuk mendeteksi plat nomor secara real-time.
- Menambahkan fitur penyimpanan hasil deteksi ke file atau database.

---

##
