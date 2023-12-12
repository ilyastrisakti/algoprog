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

print("KALKULATOR PYTHAGORAS")
sisi_dicari = input("Sisi mana yang ingin anda cari? (a, b, c) -> ")

if sisi_dicari == 'a':
    sisi_b = float(input("Masukkan panjang sisi b: "))
    sisi_c = float(input("Masukkan panjang sisi c: "))
    
    if sisi_c < sisi_b:
        print("Panjang sisi c tidak boleh lebih kecil dari sisi b.")
    else:
        sisi_a = (sisi_c**2 - sisi_b**2)**0.5
        print(f"Panjang sisi a adalah {sisi_a}")
elif sisi_dicari == 'b':
    sisi_a = float(input("Masukkan panjang sisi a: "))
    sisi_c = float(input("Masukkan panjang sisi c: "))
    
    if sisi_c < sisi_a:
        print("Panjang sisi c tidak boleh lebih kecil dari sisi a.")
    else:
        sisi_b = (sisi_c**2 - sisi_a**2)**0.5
        print(f"Panjang sisi b adalah {sisi_b}")
elif sisi_dicari == 'c':
    sisi_a = float(input("Masukkan panjang sisi a: "))
    sisi_b = float(input("Masukkan panjang sisi b: "))
    
    if sisi_b > sisi_a:
        print("Panjang sisi c tidak boleh lebih kecil dari sisi a.")
    else:
        sisi_c = (sisi_a**2 + sisi_b**2)**0.5
        print(f"Panjang sisi c adalah {sisi_c}")
else:
    print("Pilihan sisi tidak valid. Harap pilih a, b, atau c.")
