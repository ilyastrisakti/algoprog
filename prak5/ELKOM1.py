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

# Meminta input dari pengguna
jumlah_bilangan = int(input("Masukkan Jumlah Bilangan: "))
angka_pertama = int(input("Masukkan Angka Pertama: "))
angka_kedua = int(input("Masukkan Angka Kedua: "))

# Inisialisasi variabel untuk menghitung bilangan Fibonacci
bilangan_sebelumnya = angka_pertama
bilangan_sekarang = angka_kedua

# Menghitung dan menampilkan bilangan Fibonacci
for i in range(jumlah_bilangan):
    print("berikut urutannya")
    print(bilangan_sekarang)
    
    # Menghitung bilangan Fibonacci selanjutnya
    bilangan_fibonacci = bilangan_sebelumnya + bilangan_sekarang
    
    # Memperbarui bilangan_sebelumnya dan bilangan_sekarang
    bilangan_sebelumnya = bilangan_sekarang
    bilangan_sekarang = bilangan_fibonacci
