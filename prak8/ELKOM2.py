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

print("PROGRAM MENGHITUNG JUMLAH RANGE")

# Meminta pengguna memasukkan dua angka
angka_pertama = int(input("Masukkan angka pertama: "))
angka_kedua = int(input("Masukkan angka kedua: "))

# Menghitung jumlah range
jumlah_range = sum(range(angka_pertama, angka_kedua + 1))

print("Jumlah range adalah:", jumlah_range)
