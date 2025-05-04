import requests
import json


def send_file_as_payload(self):
    url = "https://httpbin.org/post"  # Contoh endpoint untuk menerima POST request

    try:
        with open("example.txt", "rb") as f:  # Buka file dalam mode binary read ('rb')
            files = {"file": ("example.txt", f, "text/plain")}
            response = requests.post(url, files=files)
            response.raise_for_status()
            print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Terjadi kesalahan: {e}")

'''
Dalam contoh ini:

Kita membuka file example.txt dalam mode binary read ("rb"). Ini memastikan kita membaca konten file sebagai bytes.
Dictionary files digunakan untuk mengirim file. Nilai untuk kunci "file" adalah tuple (filename, fileobj, content_type). fileobj adalah file object yang kita buka dalam mode binary.
requests akan mengambil konten binary dari f dan mengirimkannya sebagai bagian dari body request dengan encoding multipart/form-data.
Kesimpulan:

Ya, ketika Anda mengirim file melalui HTTP menggunakan library seperti requests, konten file akan dibaca dan dikirimkan sebagai urutan byte (binary data) dalam body request. Encoding multipart/form-data digunakan untuk mengemas data file bersama dengan metadata lainnya.
'''