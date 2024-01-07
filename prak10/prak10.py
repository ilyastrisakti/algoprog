mahasiswa=[]
def data_masuk():
   nama  = input("Masukkan Nama Mahasiswa: ")
   nilai1=int(input("Masukkan Nilai Praktikum 1: "))
   nilai2=int(input("Masukkan Nilai Praktikum 2: "))
   nilai3=int(input("Masukkan Nilai Praktikum 3: "))
   list=[nama,nilai1,nilai2,nilai3]
   mahasiswa.insert(len(mahasiswa),list)
   main()
def data():
    print(" NAMA |","PRAK 1|","PRAK 2|","PRAK 3|")
    for i in mahasiswa:
        print(i[0],"     ",i[1],"     ",i[2],"     ",i[3])
    main()
def nilaimahasiswa():
    for i in range(len(mahasiswa)):
        total=0
        for j in range (1,len(mahasiswa[i])):
            total+=mahasiswa[i][j]
        print(mahasiswa[i][0],"=",total/len(mahasiswa[i]))
    main()
def nilaipraktikum():
    praktikum1=0
    praktikum2=0
    praktikum3=0
    for i in range(len(mahasiswa)):
        praktikum1+=mahasiswa[i][1]
        praktikum2+=mahasiswa[i][2]
        praktikum3+=mahasiswa[i][3]
    praktikum1=praktikum1/len(mahasiswa)
    praktikum2=praktikum2/len(mahasiswa)
    praktikum3=praktikum3/len(mahasiswa)
    print("Nilai rata-rata 1= ",praktikum1)
    print("Nilai rata-rata 2= ",praktikum2)
    print("nilai rata-rata 3= ",praktikum3)
    main()
def nilairatarata():
    nama_cari = input("Masukkan Nama Mahasiswa yang ingin dicari rata-ratanya: ")
    found = False
    for i in range(len(mahasiswa)):
        if mahasiswa[i][0] == nama_cari:
            total = sum(mahasiswa[i][1:])
            rata_rata = total / len(mahasiswa[i][1:])
            print("Rata-rata nilai untuk", nama_cari, "adalah:", rata_rata)
            found = True
            break
    
    if not found:
        print("Mahasiswa dengan nama", nama_cari, "tidak ditemukan.")
    main()
def update_nilai():
    update=input("Nama Yang Dicari :")
    nilai=int(input("Ingin Update nilai Praktikum ke-: "))
    nilai_baru=int(input("Nilai Baru: "))
    for i in mahasiswa:
        if i [0]==update:
            i[nilai]=nilai_baru
    main()
def main():
    print("Program Membuat List")
    print("1.Memasukkan nama dan nilai")
    print("2.Lihat data")
    print("3.Nilai rata-rata mahasiswa")
    print("4.Nilai rata-rata setiap praktikum mahasiswa")
    print("5.Mencari nilai rata-rata dari setiap mahasiswa")
    print("6.Mengubah nilai mahasiswa")
    print("7.Keluar")
    pilih=int(input("Silahkan pilih (ketik 7 jika ingin keluar):"))
    if pilih==1:
        data_masuk()
    elif pilih==2:
        data()
    elif pilih==3:
        nilaimahasiswa()
    elif pilih==4:
        nilaipraktikum()
    elif pilih==5:
        nilairatarata()
    elif pilih==6:
        update_nilai()
    elif pilih==7:
        exit()
    else:
        print("Keyword yang kamu masukan salah!")
        pilih=int(input("Silahkan pilih (ketik 7 jika ingin keluar):"))
main()