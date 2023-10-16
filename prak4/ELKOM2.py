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

#Membuat list angka
angka = []

#user input jumlah angka
input_angka = input("Masukkan List Angka (integer) -> ")

#Membagi input pengguna menjadi angka-angka
angka_input = input_angka.split()

#Mengonversi angka-angka menjadi integer dan menyimpannya dalam list
for angka_str in angka_input:
    angka.append(int(angka_str))

#verifikasi list jika terdapat angka genap atau tidak
terdapat_genap = False

for num in angka:
    if num % 2 == 0:
        terdapat_genap = True
        break

if terdapat_genap:
    print("List memiliki angka genap.")
else:
    print("List tidak memiliki angka genap.")