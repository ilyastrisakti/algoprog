import sys

def awal():
    try:
        with open('contoh.txt', 'r') as f:
            print("File ditemukan.")
            main()
    except FileNotFoundError:
        print("File tidak ditemukan.")

def simpan():
    # Simpan perubahan
    text_file = open("contoh.txt", "r")
    text_file.close()
    main()

def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)

def cari_rata_rata():
    with open('contoh.txt', 'r') as f:
        lines = f.readlines()
        nilai_praktikum = []
        for line in lines:
            parts = line.split()
            nilai = [int(part) for part in parts[1:]]
            nilai_praktikum.extend(nilai)

        rata_rata = hitung_rata_rata(nilai_praktikum)
        print(f"Rata-rata nilai praktikum mahasiswa: {rata_rata}")
        main()

def update_nilai():
    print("[3. UPDATE NILAI PRAKTIKUM MAHASISWA]")
    nama = input("Masukkan nama mahasiswa: ")
    nomor_nilai = int(input("Ingin update nilai prak ke-: "))
    nilai_baru = int(input("Nilai baru: "))

    with open('contoh.txt', 'r') as f:
        lines = f.readlines()
    
    if nomor_nilai <= len(lines):
        lines[nomor_nilai - 1] = f"{nama} {nilai_baru}\n"
        
        with open('contoh.txt', 'w') as f:
            f.writelines(lines)
        
        print("DATA BERHASIL DI UPDATE.")
    else:
        print("Nomor nilai tidak valid.")
    
    main()

def main():
    print('''
    [MENU]
    1. Baca Data
    2. Cari Nilai Rata-rata Praktikum Mahasiswa
    3. Update Nilai Praktikum Mahasiswa
    4. Simpan Perubahan
    5. Exit
    ''')
    choose_menu = int(input('Silahkan Pilih: '))
    if choose_menu == 1:
        with open('contoh.txt', 'r') as f:
            print(f.read())
            main()
    elif choose_menu == 2:
        cari_rata_rata()
    elif choose_menu == 3:
        update_nilai()
    elif choose_menu == 4:
        simpan()
        main()
    elif choose_menu == 5:
        sys.exit(0)

if __name__ == '__main__':
    awal()
    main()
