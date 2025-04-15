# Program menghitung gaji total berdasarkan status dan golongan

print("Program Menghitung Gaji Total Berdasarkan Status dan Golongan")

def hitung_gaji():
    # Input data pegawai
    print("Mohon Masukkan Data Diri Anda")
    nama = input("Masukkan Nama: ")
    nik = input("Masukkan NIK: ")
    status = input("Masukkan Status (Pegawai Tetap/Honor): ").strip().lower()
    golongan = input("Masukkan Golongan (A/B/C): ").strip().upper()
    
    # Daftar gaji dan bonus
    gaji_tetap = 1000000
    gaji_honor = 750000
    bonus_tetap = {'A': 200000, 'B': 400000, 'C': 550000}
    bonus_honor = {'A': 150000, 'B': 275000, 'C': 480000}
    
    # Menentukan gaji dan bonus berdasarkan status dan golongan
    if status == "tetap":
        gaji = gaji_tetap
        bonus = bonus_tetap.get(golongan, 0)
    elif status == "honor":
        gaji = gaji_honor
        bonus = bonus_honor.get(golongan, 0)
    else:
        print("Status pegawai tidak valid.")
        return
    
    # Menghitung total gaji
    total_gaji = gaji + bonus
    
    # Menampilkan hasil
    print("\n===== Slip Gaji =====")
    print(f"Nama      : {nama}")
    print(f"NIK       : {nik}")
    print(f"Status    : {status.capitalize()}")
    print(f"Golongan  : {golongan}")
    print(f"Gaji      : Rp {gaji:,}")
    print(f"Bonus     : Rp {bonus:,}")
    print(f"Gaji Total: Rp {total_gaji:,}")

# Menjalankan program
hitung_gaji()
