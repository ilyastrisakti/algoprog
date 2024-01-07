import sys

def baca_data(data):
    print("Daftar Nama dan Nilai")
    for line in data:
        dataline = line.strip().split(' ')
        nama = dataline[0]
        nilai = ' '.join(dataline[1:])
        print(f"{nama} = {nilai}")

def nilai_rata_rata(data):
    input_nama = input("Masukkan nama mahasiswa: ")
    found = False
    for line in data:
        dataline = line.strip().split(' ')
        nama = dataline[0]
        if input_nama == nama:
            nilai = ' '.join(dataline[1:])
            rata_rata = sum(map(int, dataline[1:])) / len(dataline[1:])
            print(f"Nilai: {nilai} (rata-rata: {rata_rata})")
            found = True
    if not found:
        print("Nama mahasiswa tidak ditemukan.")

def ubah_nilai(data):
    input_nama = input("Masukkan nama mahasiswa: ")
    nilai_baru = input("Masukkan nilai baru: ")
    try:
        nilai_baru = int(nilai_baru)
    except ValueError:
        print("Masukkan angka untuk nilai baru.")
        return
    found = False
    for idx, line in enumerate(data):
        dataline = line.strip().split(' ')
        nama = dataline[0]
        if input_nama == nama:
            data[idx] = f"{nama} {nilai_baru}\n"
            print("Berhasil Diupdate!")
            found = True
    if not found:
        print("Nama mahasiswa tidak ditemukan.")

def simpan_data(file_name, data):
    try:
        with open(file_name, 'w') as file:
            file.writelines(data)
        print("Perubahan berhasil disimpan.")
    except IOError:
        print("Gagal menyimpan perubahan.")

def main():
    file_name = input("Masukkan nama file: ")
    
    try:
        with open(file_name, 'r') as file:
            data = file.readlines()
    except FileNotFoundError:
        print("File tidak ditemukan.")
        sys.exit()

    while True:
        print(f"\t======{file_name}======")
        print(" 1. Baca Data\n 2. Mencari Rata-Rata Nilai Praktikum\n 3. Update Nilai Praktikum\n 4. Simpan Perubahan Nilai\n 5. Keluar")
        menu = int(input("Mau yang mana: "))
        if menu == 1:
            baca_data(data)
        elif menu == 2:
            nilai_rata_rata(data)
        elif menu == 3:
            ubah_nilai(data)
        elif menu == 4:
            simpan_data(file_name, data)
        elif menu == 5:
            break

if __name__ == "__main__":
    main()
