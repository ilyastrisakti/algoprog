# Meminta input dari pengguna (string 4 karakter dalam huruf kecil)
input_string = input("Masukkan string 4 karakter dalam huruf kecil: ")

# Pastikan panjang string adalah 4 karakter
if len(input_string) != 4:
    print("Masukkan harus berupa 4 karakter.")
else:
    # Mengkonversi string ke kode bilangan desimal (ASCII)
    bilangan_desimal = [ord(char) for char in input_string]

    # Menambahkan sejumlah angka untuk mengubah string menjadi huruf besar
    for i in range(4):
        bilangan_desimal[i] -= 32

    # Mengubah bilangan desimal kembali menjadi string
    string_hasil = ''.join([chr(bilangan) for bilangan in bilangan_desimal])

    # Menampilkan hasil kapitalisasi
    print(f"Hasil kapitalisasi: {string_hasil}")
