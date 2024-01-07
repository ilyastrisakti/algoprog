# Fungsi untuk menghitung jumlah string yang memenuhi syarat
def hitung_string_sesuai_kriteria(input_list):
    count = 0
    for string in input_list:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

# Input list
input_list = input("Masukkan list string dipisahkan oleh spasi: ").split()

# Menghitung jumlah string yang memenuhi syarat
jumlah_string = hitung_string_sesuai_kriteria(input_list)

# Menampilkan hasil
print(f"terdapat {jumlah_string} string yang memenuhi syarat")