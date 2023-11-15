#WM program
print('''
@@@@  @@    @@       @@   @@@    @@@@@@  
 @@   @@      @@   @@   @@ @@    @@  @@ 
 @@   @@       @@@@    @@   @@   @@       
 @@   @@        @@    @@     @@  @@@@@@  
 @@   @@        @@    @@@@@@@@@      @@ 
 @@   @@        @@    @@     @@  @@   @@ 
@@@@  @@@@      @@    @@     @@  @@@@@@  
''')

kalimat = input("Masukkan sesuatu: ").lower()  # Mengonversi input ke huruf kecil untuk mempermudah perhitungan

# Menginisialisasi variabel jumlah huruf vokal dan konsonan
jumlah_vokal = 0
jumlah_konsonan = 0

# Mengecek setiap karakter dalam kalimat
for karakter in kalimat:
    if karakter.isalpha():  # Hanya memproses karakter huruf
        if karakter in "aeiou":
            jumlah_vokal += 1
        else:
            jumlah_konsonan += 1

# Menampilkan hasil
print("Jumlah huruf vokal:", jumlah_vokal)
print("Jumlah huruf konsonan:", jumlah_konsonan)
