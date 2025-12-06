import os
import datetime

# database
user = {
    "irfan": "9651",
    "wildan": "9783"
}
data_kegiatan ={
    "irfan": [],
    "wildan": []
}
# bantuan library dan dekorasi program
def pembersih_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def dekorasi(teks):
    lebar = 52
    print("=" * lebar)
    for i in range(3):
        if i == 1:
            sisa = lebar - 2 - len(teks)
            kiri = sisa // 2
            kanan = sisa - kiri
            print("|" + " " * kiri + teks + " " * kanan + "|")
        else:
            print("|" + " " * (lebar - 2) + "|")
    print("=" * lebar)

def validasi_tanggal(angka, harus=True):
    while True:
        tanggal_input = input(angka)
        if not harus and tanggal_input.strip() == "":
            return ""
        if harus and tanggal_input.strip() == "":
            print("   [!] Error: Input tidak boleh kosong (Enter). Harap isi tanggal.")
            continue

        else:
            try:
                datetime.datetime.strptime(tanggal_input, "%d-%m-%Y")
                return tanggal_input
            except ValueError:
                print("   [!] Error: Format salah/Tanggal tidak valid! Gunakan format dd-mm-yyyy (Cth: 12-10-2023).")

# sistem validasi

def validasi_angka(angka):
    while True:
        data = input(angka)
        if data.strip() == "":
            print("   [!] Error: Input tidak boleh kosong (Enter). Harap isi angka.")
        elif not data.isdigit():
            print("   [!] Error: Input harus berupa ANGKA, tidak boleh huruf!")
        else:
            return int(data)
        
def validasi_teks(angka, harus=True, tolak_angka=False):
    while True:
        data = input(angka)
        if harus and data.strip() == "":
            print("   [!] Error: Data ini wajib diisi! Tidak boleh kosong.")
        elif tolak_angka and data.isdigit():
            print("   [!] Error: Input tidak valid. Jangan masukkan angka saja.")
        else:
            return data
        
def validasi_prioritas():
    print("\n   Pilih Tingkat Prioritas:")
    print("   1. Tinggi (***)")
    print("   2. Sedang (**)")
    print("   3. Rendah (*)")
    
    while True:
        pilihan = input("   Masukkan pilihan (1-3): ")
        if pilihan == "1":
            return "***"
        elif pilihan == "2":
            return "**"
        elif pilihan == "3":
            return "*"
        else:
            print("   [!] Error: Hanya boleh pilih 1, 2, atau 3!")

def validasi_kategori():
    print("\n   Pilih Kategori Kegiatan:")
    print("   1. Kuliah")
    print("   2. Kerja")
    print("   3. Pribadi")
    print("   4. Lainnya (Input Manual)")
    
    while True:
        pilihan = input("   Masukkan pilihan (1-4): ")
        if pilihan == "1":
            return "Kuliah"
        elif pilihan == "2":
            return "Kerja"
        elif pilihan == "3":
            return "Pribadi"
        elif pilihan == "4":
            return input("   Masukkan Nama Kategori Baru: ")
        else:
            print("   [!] Error: Pilihan tidak valid. Pilih 1-4.")

# fitur  register dan login

def register():
    pembersih_terminal()
    dekorasi("REGISTRASI AKUN BARU")

    print("   Silakan isi data untuk mendaftar.")

    while True:
        username_baru = validasi_teks("   Masukkan Username baru: ")

        if username_baru in user:
            print(f"   [!] Username '{username_baru}' sudah terpakai! Coba buat yang lain.")
        elif username_baru.strip()=="":
            print("   [!] Error: Input tidak boleh kosong (Enter). Harap isi username.")
        elif username_baru.isdigit():
            print("   [!] Error: Username tidak boleh berupa angka!")
        else:
            break

    while True:
        print("\n (Password harus berupa angka, maksimal 4 digit)")
        password_baru = input("   Buat Password baru: ")

        if len(password_baru) == 0:
            print("   [!] Error: Password tidak boleh kosong!")
            
        elif not password_baru.isdigit():
            print("   [!] Error: Password hanya boleh berisi ANGKA (0-9)!")
        
        elif len(password_baru) != 4:
            print(f"   [!] Password harus 4 digit! Kamu memasukkan {len(password_baru)} digit.")
            
        else:
            break

    user[username_baru] =  password_baru
    data_kegiatan[username_baru] = []

    print("\n   [v] Registrasi berhasil!")
    print(f"   Akun '{username_baru}' telah dibuat.")
    print("\n   Tekan [Enter] untuk kembali ke Menu Awal.")

def login():
    pembersih_terminal()
    dekorasi("SISTEM LOGIN")

    percobaan = 0
    while percobaan < 3:
        username = input("Username: ")
        password = input("Password: ")
        if username in user and user[username] == password:
            print(f"\n   [v] Login Berhasil! Halo, {username}.")
            input("   [Tekan Enter untuk lanjut ke Menu...]")
            return username
        else:
            print("   [x] Username atau Password salah!")
            percobaan += 1
    
    print("   [!] Akses Ditolak. Terlalu banyak percobaan.")
    input("   Tekan [Enter] untuk kembali.")
    return None

# fitur CRUD

def tambah_kegiatan(users):
    pembersih_terminal()
    dekorasi("TAMBAH KEGIATAN")

    judul = validasi_teks("Nama Kegiatan(Tugas,Kebiasaan, dll): ", harus=True)
    kategori = validasi_kategori()
    print()
    awal  = validasi_tanggal("Tanggal Mulai (dd-mm-yyyy): ", harus=True)

    print("   [Enter] jika deadline sama dengan tanggal mulai")
    akhir = validasi_tanggal("Deadline (dd-mm-yyyy): ", harus=False)

    if akhir == "":
        deadline = awal
        print(f"Deadline otomatis diatur ke: {akhir}")
    else:
        deadline = akhir

    prioritas = validasi_prioritas()
    print("\n   (Masukkan Catatan, tekan[Enter] jika ingin mengosongkan.)")
    catatan = input("Catatan: ")
    if catatan.strip() == "":
        catatan = "-"

    kegiatan_baru ={
        "judul": judul,
        "kategori": kategori,
        "mulai": awal,
        "deadline": deadline,
        "prioritas": prioritas,
        "catatan": catatan,
        "status": False
        }

    data_kegiatan[users].append(kegiatan_baru)
    print("\n   [v] Kegiatan berhasil disimpan!")
    input("   Tekan [Enter] untuk kembali ke Menu Utama.")

def tampilkan_kegiatan(users, filter_judul=None):
    pembersih_terminal()
    header = "DAFTAR KEGIATAN" if not filter_judul else f"PENCARIAN: {filter_judul}"
    dekorasi(header)

    kegiatan_user = data_kegiatan[users]

    if not kegiatan_user:
        print("   [!] Belum ada kegiatan yang tersimpan.")
        if not filter_judul:
            input("\n   [Tekan Enter untuk kembali...]")
        return
    def cek_urutan_prioritas(kegiatan):
        if kegiatan['prioritas'] == '***':
            return 1
        elif kegiatan['prioritas'] == '**':
            return 2
        elif kegiatan['prioritas'] == '*':
            return 3
        else:
            return 99
    tugas_diurutkan = sorted(kegiatan_user, key=cek_urutan_prioritas)
    nomor = 1
    ditemukan = False

    for kegiatan in tugas_diurutkan:
        if filter_judul:
            keyword = filter_judul.lower()

            cek_judul = keyword in kegiatan['judul'].lower()
            cek_kategori = keyword in kegiatan['kategori'].lower()
            cek_mulai = keyword in kegiatan['mulai']
            cek_deadline = keyword in kegiatan['deadline']

            if not (cek_judul or cek_kategori or cek_mulai or cek_deadline):
                continue
            
        ditemukan = True
        catatan_tampil = kegiatan['catatan']
        status_tandai = "[SELESAI]" if kegiatan['status'] else "[BELUM]"
        prio_ini = kegiatan['prioritas']
        kat_ini = kegiatan['kategori'].upper()

        print(f"{nomor}. {kegiatan['judul']} {status_tandai}")
        print(f"    Kategori    : {kat_ini}")
        print(f"    Prioritas   : {prio_ini}")
        print(f"    Waktu       : {kegiatan['mulai']} s/d {kegiatan['deadline']}")
        print(f"    Catatan     : {catatan_tampil}")

        if not kegiatan['status']:

            if kegiatan['prioritas'] == '***':
                print("    [!!] PERINGATAN: Prioritas TINGGI! Kerjakan segera!")
            else:
                print("    >>> AYO KERJAKAN! Kegiatan ini belum selesai.")
            
        print("-" * 52)
        nomor += 1
    if filter_judul and not ditemukan:
        print(f"   [!]Tidak ada Kegiatan yang cocok dengan pencarian '{filter_judul}'.")

    if not filter_judul:
        input("\n   Tekan [Enter] untuk kembali ke Menu Utama.")

def ubah_kegiatan(users):
    pembersih_terminal()
    dekorasi("EDIT KEGIATAN")

    tugas_user = data_kegiatan[users]
    
    if not tugas_user:
        print("   [!] Data kosong, tidak ada yang bisa diedit.")
        input("   [Enter] untuk kembali.")
        return
    for i, t in enumerate(tugas_user):
        print(f"{i+1}. {t['judul']} ({t['kategori']})")

    print("\n   0. Batal")
    pilihan = validasi_angka("   Pilih nomor kegiatan yang akan diedit: ")
    
    if pilihan == 0:
        return
    index = pilihan - 1
    if 0 <= index < len(tugas_user):
        target = tugas_user[index]
        print(f"\n   >>> Sedang mengedit: {target['judul']}")
        print("   (Biarkan KOSONG & Tekan [Enter] jika tidak ingin mengubah data)")

        print(f"\n   Nama Kegiatan Lama: {target['judul']}")
        judul_baru = input("   Nama Kegiatan Baru: ")
        if judul_baru.strip() != "":
            target['judul'] = judul_baru

        print(f"\n   Kategori Lama: {target['kategori']}")
        ubah_kat = input("   Ubah Kategori? (y/n): ").lower()
        if ubah_kat == 'y':
            target['kategori'] = validasi_kategori()

        print(f"\n   Tanggal Mulai Lama: {target['mulai']}")
        mulai_baru = validasi_tanggal("   Tanggal Mulai Baru (dd-mm-yyyy): ", harus=False)
        if mulai_baru != "":
            target['mulai'] = mulai_baru

        print(f"\n   Tanggal Deadline Lama: {target['deadline']}")
        print("   Tekan [Enter] jika deadline di tanggal yang sama.")
        deadline_baru = validasi_tanggal("   Tanggal Deadline Baru (dd-mm-yyyy): ", harus=False)
        if deadline_baru != "":
            target['deadline'] = deadline_baru
        elif mulai_baru != "":
            target['deadline'] = mulai_baru

        print(f"\n   Prioritas Lama: {target['prioritas']}")
        ganti_prio = input("   Ubah Prioritas? (y/n): ").lower()
        if ganti_prio == 'y':
            target['prioritas'] = validasi_prioritas()

        print(f"\n   Catatan Lama: {target['catatan']}")
        catatan_baru = input("   Catatan Baru: ")
        if catatan_baru.strip() != "":
            target['catatan'] = catatan_baru

        print("\n   Data yang baru berhasil tersimpan.")
    else:
        print("\n   [!] Nomor kegiatan tidak ditemukan.")

    input("   Tekan [Enter] untuk kembali ke Menu Utama.")

def aksi_fitur(users, tanda="selesai"):
    pembersih_terminal()
    header = "TANDAI SELESAI" if tanda == "selesai" else "HAPUS KEGIATAN"
    dekorasi(header)
    
    tugas_user = data_kegiatan[users]
    for i, t in enumerate(tugas_user):
        status = "SELESAI" if t['status'] else "BELUM"
        print(f"{i+1}. [{status}] {t['judul']} ({t['kategori']})")

    if not tugas_user:
        print("   Data kosong.")
        input("   [Enter] untuk kembali.")
        return
    print("\n   0. Batal/Kembali")
    pilihan = validasi_angka("   Pilih nomor kegiatan yang akan ditandai: ")
    
    if pilihan == 0:
        return
    
    index = pilihan - 1
    if 0 <= index < len(tugas_user):
        target = tugas_user[index]
        
        if tanda == "selesai":
            target['status'] = True
            print(f"\n   [v] Kegiatan '{target['judul']}' telah ditandai SELESAI.")
        elif tanda == "hapus":
            terhapus = tugas_user.pop(index)
            print(f"\n   [x] Kegiatan '{terhapus['judul']}' BERHASIL DIHAPUS.")
    else:
        print("\n   [!] Nomor tidak ditemukan.")
    
    input("   Tekan [Enter] untuk kembali.")

def cari_kegiatan(users):
    pembersih_terminal()
    dekorasi("CARI KEGIATAN")
    while True:
        print("bisa cari berdasarkan Judul, Tanggal (dd-mm-yyyy), atau Kategori.")
        keyword = input("   Masukkan kata kunci: ")

        if keyword.strip() == "":
            print("\n   [!] Kata kunci tidak boleh kosong.")
        else:
            tampilkan_kegiatan(users, filter_judul=keyword)
            input("\n   Tekan [Enter] untuk kembali.")
            return

def menu_utama(users):
    while True:
        pembersih_terminal()
        dekorasi(f"USER: {users}")
        print("1. Tambah Kegiatan")
        print("2. Tampilkan Daftar Kegiatan")
        print("3. Edit / Perbarui Kegiatan")
        print("4. Hapus Kegiatan")
        print("5. Cari Kegiatan")
        print("6. Tandai Selesai")
        print("7. Log Out")

        pilih = input("\nPilih menu (1-7): ")
        if pilih == "1":
            tambah_kegiatan(users)
        elif pilih == "2":
            tampilkan_kegiatan(users)
        elif pilih == "3":
            ubah_kegiatan(users)
        elif pilih == "4":
            aksi_fitur(users, "hapus")
        elif pilih =="5":
            cari_kegiatan(users)
        elif pilih =="6":
            aksi_fitur(users, "selesai")
        elif pilih =="7":
            return "logout"
        else:
            print("[!] Pilihan tidak valid.")
            input("[Tekan Enter untuk kembali]")

# Perulangan Utama
while True:
    pembersih_terminal()
    dekorasi("APLIKASI TO-DO LIST")
    print("   Selamat Datang! Apakah anda sudah punya akun?")
    print("   1. Sudah (Login)")
    print("   2. Belum (Register)")
    print("   3. Keluar Aplikasi")

    pilihan = input("\n   Masukkan pilihan (1-3): ")
        
    if pilihan == "1":
        user_aktif = login()
        if user_aktif:
            menu_utama(user_aktif)
        
    elif pilihan == "2":
        register()
            
    elif pilihan == "3":
        print("   Terima kasih telah menggunakan aplikasi ini.")
        break
            
    else:
        print("   [!] Pilihan tidak valid.")
        input("   [Enter] untuk ulangi.")