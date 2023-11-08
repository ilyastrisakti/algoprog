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

# input nilai
v0 = float(input("Masukkan v0= "))
t = float(input("Masukkan t= "))
a = float(input("Masukkan a= "))

# rumus hitung
s = v0 * t + 0.5 * a * t**2

# print hasil
print(f"Jarak tempuh jika kecepatan awal adalah {v0} m/s, percepatan {a} m/s^2, dan waktu {t} s maka jarak tempuh adalah {s} meter.")