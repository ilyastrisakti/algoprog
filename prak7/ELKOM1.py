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

def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n-1)

nilai = int(input("Masukkan nilai: "))
hasil_faktorial = faktorial(nilai)

print(f"Faktorial dari {nilai} adalah {hasil_faktorial}")
