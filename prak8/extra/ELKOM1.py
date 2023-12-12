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

def cekBil(bil):
    if bil == 1:
        print(bil,"= prima")
    elif bil == 2:
        print(bil,"= prima")
    else:
        global x
        for x in range(2,bil):
            if bil%x==0:
                stat = 0
                break
            else:
                stat = 1
        cekStat(stat)
        
def cekStat(stat):
    if stat == 0:
        print(bil,"= bukan prima")
        print(f"{x} x {bil//x} = {bil}")
    else:
        print(bil,"= prima")   
while True:
    print()
    bil = int(input("Masukan angka:"))
cekBil(bil)
