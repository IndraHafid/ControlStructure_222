# Tulis program PYTHON untuk mencetak bilangan ganjil hingga n!

def cetak_bilangan_ganjil(n):
    print("[", end="") 
    for i in range(1, n+1):
        if i % 2 != 0:
            print(i, end=" ")  # Mencetak bilangan ganjil 
    print("]") 

n = int(input("Masukkan nilai n untuk batas bilangan ganjil: ")) 

cetak_bilangan_ganjil(n)