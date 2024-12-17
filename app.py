import cv2
import pytesseract
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Path ke Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Fungsi untuk memproses gambar
def process_image(file_path):
    try:
        # Baca gambar
        image = cv2.imread(file_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(blur, 50, 200)

        # Cari kontur
        contours, _ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
            if len(approx) == 4:  # Cari kontur persegi panjang
                x, y, w, h = cv2.boundingRect(approx)

                # Threshold untuk ukuran plat nomor
                if w > 50 and h > 20:
                    plate = gray[y:y+h, x:x+w]

                    # Resize area plat nomor
                    plate_resized = cv2.resize(plate, (300, 100), interpolation=cv2.INTER_CUBIC)

                    # OCR untuk membaca teks dari area plat nomor
                    text = pytesseract.image_to_string(plate_resized, config='--psm 8')

                    # Simpan gambar hasil pemrosesan sementara
                    cv2.imwrite("temp_plate.jpg", plate_resized)

                    return "temp_plate.jpg", text.strip()

        return None, "No License Plate Detected"

    except Exception as e:
        messagebox.showerror("Error", f"Error processing image: {str(e)}")
        return None, None

# Fungsi untuk memilih file
def choose_file():
    file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.tiff")]
    )
    if file_path:
        # Proses gambar
        plate_path, detected_text = process_image(file_path)

        if plate_path:
            # Tampilkan hasil gambar di GUI
            display_image(plate_path)

            # Tampilkan hasil teks
            result_label.config(text=f"Detected Text: {detected_text}")
        else:
            result_label.config(text="No License Plate Detected")

# Fungsi untuk menampilkan gambar di GUI
def display_image(image_path):
    image = Image.open(image_path)
    image = image.resize((300, 100), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    # Tampilkan di label
    image_label.config(image=photo)
    image_label.image = photo

# GUI Tkinter
root = tk.Tk()
root.title("Pengenalan Plat Nomor Kendaraan")
root.geometry("600x500")
root.resizable(False, False)

# Label judul
tk.Label(root, text="Pengenalan Plat Nomor Kendaraan", font=("Helvetica", 18)).pack(pady=20)

# Tombol "Choose Image"
choose_button = tk.Button(root, text="Choose Image", command=choose_file, font=("Helvetica", 12), bg="#4CAF50", fg="white")
choose_button.pack(pady=10)

# Label untuk menampilkan gambar hasil pemrosesan
image_label = tk.Label(root)
image_label.pack(pady=20)

# Label untuk hasil teks
result_label = tk.Label(root, text="", font=("Helvetica", 14), fg="blue")
result_label.pack(pady=10)

# Jalankan aplikasi GUI
root.mainloop()
