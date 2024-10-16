# Tulis program PYTHON untuk menghasilkan desain berikut
# 1
# 2 2
# 3 3 3
# 4 4 4 4 
# 5 5 5 5 5
# Jika pengguna memasukkan nilai n sebagai 5
  
n = 5 

for i in range(1, n+1):
    for j in range(i):
        print(i, end=" ") # Mencetak angka pada baris yang sama
    print() 
