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

print("PROGRAM MENEMUKAN ANGKA TERBESAR")
angka1 = float(input("Masukkan angka ke-1: "))
angka2 = float(input("Masukkan angka ke-2: "))
angka3 = float(input("Masukkan angka ke-3: "))

angka_terbesar = max(angka1, angka2, angka3)

print(f"Angka terbesarnya adalah: {angka_terbesar}")