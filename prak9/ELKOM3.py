# Fungsi untuk menghitung hasil kali seluruh nilai dalam list
def hitung_hasil_kali(input_list):
    hasil_kali = 1
    for nilai in input_list:
        hasil_kali *= nilai
    return hasil_kali

# Input list
input_list = [int(x) for x in input("Masukkan list angka dipisahkan oleh spasi: ").split()]

# Menghitung hasil kali nilai dalam list
hasil = hitung_hasil_kali(input_list)

# Menampilkan hasil
print("ELKOM 3")
print(f"hasil kali seluruh value pada list adalah: {hasil}")
