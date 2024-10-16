# Tulis program PYTHON untuk mengevaluasi kinerja siswa
    # Jika % >= 90  maka Kinerja sangat baik
    # Jika % >= 80  maka kinerja Sangat Baik
    # Jika % >= 70  maka Kinerja baik
    # Jika % >= 60  maka kinerja rata-rata

nilai = input("Masukkan Nilai: ")

nilai = int(nilai)
if nilai >= 90:
    print("Kinerja sangat baik")
elif nilai >= 80:
    print("Kinerja sangat baik")
elif nilai >= 70:
    print("Kinerja baik")
elif nilai >= 60:
    print("Kinerja rata-rata")
else:
    print("Kinerja perlu ditingkatkan")
    
    