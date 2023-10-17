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

# Meminta input koordinat pertama dan kedua
input_koordinat_pertama = input("Masukkan angka pertama (x1, y1): ")
input_koordinat_kedua = input("Masukkan angka kedua (x2, y2): ")

# Mengonversi input ke dalam angka float dengan tanda koma sebagai pemisah
x1, y1 = map(float, input_koordinat_pertama.split(','))
x2, y2 = map(float, input_koordinat_kedua.split(','))

# Menghitung jarak antara dua titik koordinat
jarak = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# Menampilkan hasil perhitungan jarak
print(f"Jarak antara ({x1}, {y1}) dan ({x2}, {y2}) adalah {jarak:.2f}")

