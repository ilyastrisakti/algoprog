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

def pangkat_kubik(angka):
    return angka ** 3

def cek_habis_dibagi_tiga(angka):
    if angka % 3 == 0:
        return pangkat_kubik(angka)
    else:
        return False

nilai = int(input("Masukkan nilai: "))

hasil = cek_habis_dibagi_tiga(nilai)

if hasil:
    print(f"Hasilnya adalah {hasil}")
else:
    print("False")