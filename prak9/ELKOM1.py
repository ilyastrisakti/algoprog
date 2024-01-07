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

# Meminta pengguna memasukkan list integer
list_integer = input("Masukkan list integer (pisahkan angka dengan spasi): ").split()
list_integer = [int(x) for x in list_integer]

# Mengonversi list menjadi tuple dan melakukan reverse
tuple_reverse = tuple(list_integer[::-1])

print("Hasil reverse ke tuple:")
print(tuple_reverse)

# Menampilkan list awal dan tuple hasil reverse
print(f"(list tuple): {list_integer}, {tuple_reverse}")
