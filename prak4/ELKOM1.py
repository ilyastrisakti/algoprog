print('''
@@@@  @@    @@       @@   @@@    @@@@@@  
 @@   @@      @@   @@   @@ @@    @@  @@ 
 @@   @@       @@@@    @@   @@   @@       
 @@   @@        @@    @@     @@  @@@@@@  
 @@   @@        @@    @@@@@@@@@      @@ 
 @@   @@        @@    @@     @@  @@   @@ 
@@@@  @@@@      @@    @@     @@  @@@@@@  
''')

# Fungsi untuk mengkonversi desimal ke biner
def desimal_ke_biner():
    angka_desimal = int(input("Masukkan angka: "))
    angka_biner = bin(angka_desimal)
    print(f"Angka {angka_desimal} dalam biner adalah {angka_biner[2:]}")

# Fungsi untuk mengkonversi biner ke desimal
def biner_ke_desimal():
    angka_biner = input("Masukkan biner: ")
    angka_desimal = int(angka_biner, 2)
    print(f"Angka {angka_biner} dalam desimal adalah {angka_desimal}")

# Loop utama program
while True:
    
    print("----PROGRAM KONVERSI BILANGAN----")
    print("1 -> Angka ke Biner")
    print("2 -> Biner ke Angka")
    print("3 -> Exit")
    
    pilihan = input("Masukan Pilihan Anda-> ")
    
    if pilihan == '1':
        desimal_ke_biner()
    elif pilihan == '2':
        biner_ke_desimal()
    elif pilihan == '3':
        print("Terimakasih telah menggunakan program ini.")
        break
    else:
        print("err.")
