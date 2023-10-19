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

# Meminta input jam masuk kerja dan mengucapkan "Selamat Pagi"
jam_masuk = input("Jam masuk kerja (HH MM): ").split()
jam_masuk = int(jam_masuk[0]) + int(jam_masuk[1]) / 60
print("Selamat Pagi")

# Meminta input jam keluar kerja dan mengucapkan "Selamat Malam"
jam_keluar = input("Jam keluar kerja (HH MM): ").split()
jam_keluar = int(jam_keluar[0]) + int(jam_keluar[1]) / 60
print("Selamat Malam")

# Menghitung waktu kerja dalam jam
waktu_kerja = jam_keluar - jam_masuk

# Gaji per hari
gaji_perhari = 175000  # Gaji per hari (tanpa lembur)

# Menghitung lembur dan total gaji
lembur = 0
if waktu_kerja > 8:
    lembur = (waktu_kerja - 8) * 15000

total_gaji = gaji_perhari + lembur

# Menampilkan rincian gaji
print("\n-----Rincian Gaji-----")
print(f"Waktu kerja:\t{waktu_kerja:.2f} jam ({jam_masuk} sd {jam_keluar})")
print(f"Gaji perhari:\tRp {gaji_perhari:,}")
print(f"Lembur:\t\tRp {lembur:,} ({(waktu_kerja - 8):.2f} jam x @Rp 15.000)")
print(f"Total Gaji:\tRp {total_gaji:,}")