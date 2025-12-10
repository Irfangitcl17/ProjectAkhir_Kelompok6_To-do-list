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

    while True:
        print("   [Enter] jika deadline sama dengan tanggal mulai")
        akhir = validasi_tanggal("Deadline (dd-mm-yyyy): ", harus=False)

        if akhir == "":
            deadline = awal
            print(f"Deadline otomatis diatur ke: {akhir}")
            break
        else:
            tgl_mulai = datetime.datetime.strptime(awal, "%d-%m-%Y")
            tgl_akhir = datetime.datetime.strptime(akhir, "%d-%m-%Y")

            if tgl_akhir < tgl_mulai:
                print("   [!] Error: Deadline tidak boleh sebelum tanggal mulai!")
                print(f"  Mulai: {awal}, tapi Deadline: {akhir}. Coba lagi.\n")
            else:
                deadline = akhir
                break

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

    list_belum = []
    list_selesai = []
    
    
    hari_ini = datetime.date.today()

    def cek_urutan_prioritas(kegiatan):
        if kegiatan['prioritas'] == '***': return 1
        elif kegiatan['prioritas'] == '**': return 2
        elif kegiatan['prioritas'] == '*': return 3
        else: return 99

    keyword = filter_judul.lower() if filter_judul else ""

    for kegiatan in kegiatan_user:
        if filter_judul:
            cek_judul = keyword in kegiatan['judul'].lower()
            cek_kategori = keyword in kegiatan['kategori'].lower()
            cek_mulai = keyword in kegiatan['mulai']
            cek_deadline = keyword in kegiatan['deadline']

            if not (cek_judul or cek_kategori or cek_mulai or cek_deadline):
                continue 
        
        if kegiatan['status'] == True:
            list_selesai.append(kegiatan)
        else:
            list_belum.append(kegiatan)

    list_belum = sorted(list_belum, key=cek_urutan_prioritas)

    
    print(f"\n   [ TUGAS AKTIF (BELUM SELESAI) ({len(list_belum)}) ]")
    print("   " + "-"*45)

    if not list_belum:
        if filter_judul:
            print("   (Tidak ditemukan tugas sesuai pencarian)")
        else:
            print("   (Tidak ada tugas aktif. Kerja bagus!)")
    else:
        nomor_urut = 1
        for t in list_belum:

            tgl_deadline_obj = datetime.datetime.strptime(t['deadline'], "%d-%m-%Y").date()
            
            selisih = (tgl_deadline_obj - hari_ini).days
            
            pesan_waktu = ""
            if selisih < 0:
                
                pesan_waktu = f" [!!! TERLAMBAT {abs(selisih)} HARI !!!]"
            elif selisih == 0:
                pesan_waktu = " [!!! DEADLINE HARI INI !!!]"
            elif selisih == 1:
                pesan_waktu = " (Besok Terakhir!)"
            else:
                pesan_waktu = f" (Sisa {selisih} hari lagi deadline mu)"

            prio_display = t['prioritas']
            prio_teks = "TINGGI" if prio_display == "***" else ("SEDANG" if prio_display == "**" else "RENDAH")

            if selisih < 0:
                print(f"   {nomor_urut}. {t['judul']} {pesan_waktu}")
            else:
                print(f"   {nomor_urut}. {t['judul']}")

            print(f"      Kategori  : {t['kategori']}")
            print(f"      Prioritas : {prio_display} ({prio_teks})")

            if selisih >= 0:
                print(f"      Deadline  : {t['deadline']} {pesan_waktu}")
            else:
                print(f"      Deadline  : {t['deadline']} (Sudah Lewat!)")

            if t['catatan'] != "-":
                print(f"      Catatan   : {t['catatan']}")

            if selisih < 0:
                print("      >>> PERINGATAN: TUGAS INI SUDAH KADALUARSA! <<<")
            elif t['prioritas'] == '***':
                print("      >>> SEGERA KERJAKAN! <<<")
            
            print("   " + "."*45)
            nomor_urut += 1
    
    print(f"\n\n   [ RIWAYAT SELESAI ({len(list_selesai)}) ]")
    print("   " + "-"*45)
    
    if not list_selesai:
        print("   (Belum ada tugas yang diselesaikan)")
    else:
        nomor_urut = 1 
        for t in list_selesai:
            print(f"   {nomor_urut}. [SELESAI] {t['judul']}")
            print(f"      Selesai pada deadline: {t['deadline']}")
            nomor_urut += 1

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
        print("   ( Tekan [Enter] jika tidak ingin mengubah data)")

        print(f"\n   Nama Kegiatan Lama: {target['judul']}")
        judul_baru = input("   Nama Kegiatan Baru: ")
        if judul_baru.strip() != "":
            target['judul'] = judul_baru

        print(f"\n   Kategori Lama: {target['kategori']}")
        ubah_kat = input("   Apakah kamu mau ubah Kategori? (y/n): ").lower()
        if ubah_kat == 'y':
            target['kategori'] = validasi_kategori()

        temp_mulai = target['mulai']

        print(f"\n   Tanggal Mulai Lama: {target['mulai']}")
        mulai_baru = validasi_tanggal("   Tanggal Mulai Baru (dd-mm-yyyy): ", harus=False)
        if mulai_baru != "":
            temp_mulai = mulai_baru

        while True:
            print(f"\n   Tanggal Deadline Lama: {target['deadline']}")
            print("   Tekan [Enter] jika deadline di tanggal yang sama.")
            deadline_baru = validasi_tanggal("   Tanggal Deadline Baru (dd-mm-yyyy): ", harus=False)
            temp_deadline = deadline_baru if deadline_baru != "" else target['deadline']

            obj_mulai = datetime.datetime.strptime(temp_mulai, "%d-%m-%Y")
            obj_deadline = datetime.datetime.strptime(temp_deadline, "%d-%m-%Y")

            if obj_deadline < obj_mulai:
                print("  [!] Error: Tanggal Deadline tidak boleh sebelum Tanggal Mulai!")
                print(f"  Mulai (Baru/Lama): {temp_mulai}")
                print(f"  Deadline yang dicoba: {temp_deadline}")
                print("  Silakan input deadline yang benar.")
            else:
                if deadline_baru != "":
                    target['deadline'] = deadline_baru
                if mulai_baru != "":
                    target['deadline'] = mulai_baru
                break

        print(f"\n   Prioritas Lama: {target['prioritas']}")
        ganti_prio = input("   Ubah Prioritas? (y/n): ").lower()
        if ganti_prio == 'y':
            target['prioritas'] = validasi_prioritas()

        ubah_cat = input("Apakah kamu ingin mengubah catatan? (y/n): ").lower()
        if ubah_cat == 'y':
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
            print(f"\n   [?] PERINGATAN: Anda akan menghapus '{target['judul']}'")
            print("       Data yang dihapus tidak bisa dikembalikan.")

            konfirmasi = input("   Yakin ingin menghapus? (ketik 'y' untuk Ya): ").lower()
            if konfirmasi == 'y':
                terhapus = tugas_user.pop(index)
                print(f"\n   [x] Kegiatan '{terhapus['judul']}' BERHASIL DIHAPUS.")
            else:
                print("\n   [!] Penghapusan DIBATALKAN. Data aman.")
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