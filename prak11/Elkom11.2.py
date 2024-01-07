import sys

file_name = input("Masukkan nama file: ")
	
file = open(file_name, 'r')
data = file.readlines()
file.close()

updates = []
	
	
def baca_data():
	print ("Daftar Nama dan Nilai")
	for line in data:
		dataline = line.strip().split(' ')
		score_1 = dataline[-3]
		score_2 = dataline[-2]
		score_3 = dataline[-1]
		nama = ' '.join(dataline[0:dataline.index(score_1)])
		print(f"{nama} = {score_1} {score_2} {score_3}")
	main()
def nilai_rata_rata():
	inputnama = input("Masukkan nama mahasiswa: ")
	for line in data:
		dataline = line.strip().split(' ')
		score_1 = dataline[-3]
		score_2 = dataline[-2]
		score_3 = dataline[-1]
		nama = ' '.join(dataline[0:dataline.index(score_1)])
		if inputnama == nama:
			rata_rata = (int(score_1) + int(score_2) + int(score_3)) / 3
			print(score_1, score_2, score_3 + f" (rata_rata: {rata_rata})")
	main()
				
def ubah_nilai():
	print ("Update Nilai")
	inputnama = input("Masukkan nama mahasiswa: ")
	nilaiKe = int(input("Update nilai praktikum ke-: "))
	nilaiBaru = int(input("Masukkan nilai baru: "))
	for line in data:
		dataline = line.strip().split(' ')
		score_1 = dataline[-3]
		score_2 = dataline[-2]
		score_3 = dataline[-1]
		nama = ' '.join(dataline[0:dataline.index(score_1)])
		if inputnama == nama:
			tempdata = [nama, int(score_1), int(score_2), int(score_3)]
			nilailama = tempdata[nilaiKe]
			tempdata[nilaiKe] = nilaiBaru
			data[data.index(line)] = f"{nama} {tempdata[1]} {tempdata[2]} {tempdata[3]}\n"
			print(f"Berhasil Diupdate!")
			updates.append(f"[{nama}] Update nilai prak {nilaiKe} | {nilailama} >> {nilaiBaru}")
	main()
def simpan_data():
	file = open(file_name, 'w')
	file.write(''.join(data))
	file.close()
	print("Perubahan berhasil disimpan.")
	main()
def keluar():
	sys.exit(0)

		
def main():
	print(f"""\t======{file_name}======
	 1. Baca Data
	 2. Mencari Rata-Rata Nilai Praktikum
	 3. Update Nilai Praktikum
	 4. Simpan Perubahan Nilai
	 5. Keluar""")
	menu = int(input("Mau yang mana: "))
	if menu == 1:
		baca_data()
	elif menu == 2:
		nilai_rata_rata()
	elif menu == 3:
		ubah_nilai()
	elif menu == 4:
		simpan_data()
	elif menu == 5:
		keluar()
if __name__ == "__main__":
	main()
