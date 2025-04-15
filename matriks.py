# Matriks A dan B berukuran 5x5
A = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

B = [
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1]
]

# Inisialisasi matriks hasil sebagai matriks kosong
hasil = []

# Perkalian matriks
for i in range(5):
    baris = []  # baris untuk hasil[i]
    for j in range(5):
        total = 0
        for k in range(5):
            total += A[i][k] * B[k][j]
        baris.append(total)
    hasil.append(baris)

# Menampilkan hasil
print("Hasil perkalian matriks A x B:")
for row in hasil:
    print(row)