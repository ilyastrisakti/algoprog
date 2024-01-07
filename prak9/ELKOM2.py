# Fungsi untuk menghitung rata-rata dari sebuah tuple
def hitung_rata_rata(tuple_data):
    total = [0] * len(tuple_data[0])  # Inisialisasi total dengan nol sejumlah elemen pada tuple pertama
    jumlah_elemen = len(tuple_data)  # Jumlah tuple di dalam tuple_data
    
    for sub_tuple in tuple_data:
        for idx, elemen in enumerate(sub_tuple.split(', ')):
            total[idx] += int(elemen)
    
    rata_rata = [round(total[i] / jumlah_elemen, 1) for i in range(len(total))]
    return rata_rata

# Tuple yang berisi beberapa tuple
tuple_data = ('1021, 1022, 1023', '1025, 1026, 1027', '1029, 1030, 1030')

# Menghitung rata-rata dari tuple
rata_rata = hitung_rata_rata(tuple_data)

# Menampilkan hasil
print("tuple 1:")
print(f"rata-rata dari tuple adalah: {rata_rata}")

#wm program
print("======= MUHAMMAD ILYAS IFADHAH =======")
print("============ 065002000023 ============")