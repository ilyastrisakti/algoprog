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

import math

def luas_permukaan_kubus(sisi):
    return 6 * sisi**2

def luas_permukaan_balok(panjang, lebar, tinggi):
    return 2 * (panjang*lebar + panjang*tinggi + lebar*tinggi)

def luas_permukaan_tabung(jari_jari, tinggi):
    return 2 * math.pi * jari_jari * (jari_jari + tinggi)

def luas_permukaan_kerucut(jari_jari, tinggi):
    garis_pelukis = math.sqrt(jari_jari**2 + tinggi**2)
    return math.pi * jari_jari * (jari_jari + garis_pelukis)

def luas_permukaan_bola(jari_jari):
    return 4 * math.pi * jari_jari**2

while True:
    print("KALKULATOR MENCARI LUAS")
    print("1. Kubus (Tambahkan sisi)")
    print("2. Balok (Tambahkan panjang, lebar, tinggi)")
    print("3. Tabung (Tambahkan jari-jari, tinggi)")
    print("4. Kerucut (Tambahkan jari-jari, tinggi)")
    print("5. Bola (Tambahkan jari-jari)")
    print("6. Keluar")

    pilihan = int(input("Mau yang mana: "))

    if pilihan == 1:
        sisi = float(input("Masukkan sisi kubus: "))
        print(f"Luas permukaan kubus dengan sisi {sisi} adalah:", luas_permukaan_kubus(sisi))
    elif pilihan == 2:
        panjang = float(input("Masukkan panjang balok: "))
        lebar = float(input("Masukkan lebar balok: "))
        tinggi = float(input("Masukkan tinggi balok: "))
        print(f"Luas permukaan balok dengan panjang {panjang}, lebar {lebar}, dan tinggi {tinggi} adalah:", luas_permukaan_balok(panjang, lebar, tinggi))
    elif pilihan == 3:
        jari_jari_tabung = float(input("Masukkan jari-jari tabung: "))
        tinggi_tabung = float(input("Masukkan tinggi tabung: "))
        print(f"Luas permukaan tabung dengan jari-jari {jari_jari_tabung} dan tinggi {tinggi_tabung} adalah:", luas_permukaan_tabung(jari_jari_tabung, tinggi_tabung))
    elif pilihan == 4:
        jari_jari_kerucut = float(input("Masukkan jari-jari kerucut: "))
        tinggi_kerucut = float(input("Masukkan tinggi kerucut: "))
        print(f"Luas permukaan kerucut dengan jari-jari {jari_jari_kerucut} dan tinggi {tinggi_kerucut} adalah:", luas_permukaan_kerucut(jari_jari_kerucut, tinggi_kerucut))
    elif pilihan == 5:
        jari_jari_bola = float(input("Masukkan jari-jari bola: "))
        print(f"Luas permukaan bola dengan jari-jari {jari_jari_bola} adalah:", luas_permukaan_bola(jari_jari_bola))
    elif pilihan == 6:
        break
    else:
        print("Pilihan tidak valid. Silakan pilih angka 1-6.")