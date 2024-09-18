from colorama import Fore, Style
from tabulate import tabulate
import pyfiglet
import pwinput

# Data Awal Siswa
no_id = ['00001', '00002', '00003', '00004', '00005', '00006', '00007', '00008', '00009', '00010', '00011', '00012', '00013', '00014', '00015', '00016', '00017', '00018', '00019', '00020']
nama_siswa = ['Andi Setiawan', 'Budi Santoso', 'Citra Dewi', 'Dodi Pratama', 'Ganjar Prasetyo', 'Hani Wijaya', 'Iwan Kurniawan', 'Joko Susilo', 'Kiki Amalia', 'Lina Marlina', 'Mira Sari', 'Nina Rahmawati', 'Omar Syahputra', 'Putu Wibowo', 'Qori Maulana', 'Rina Sari', 'Siti Nurhaliza', 'Toni Saputra', 'Umar Zulkarnain', 'Vina Anggraini']
nilai_siswa = [85, 90, 78, 68, 55, 88, 92, 74, 60, 82, 77, 69, 95, 80, 73, 85, 67, 91, 76, 84]
kelas_siswa = ['10a', '10b', '10a', '10c', '10b', '10a', '10b', '10c', '10d', '10f', '10e', '10f', '10e', '10d', '10e', '10f', '10e', '10d', '10e', '10f']
umur_siswa = [15, 16, 15, 17, 16, 15, 16, 17, 15, 16, 17, 15, 16, 17, 15, 16, 17, 15, 16, 17]
alamat_siswa = [
    'Jl. Merdeka No. 1, Jakarta',
    'Jl. Sudirman No. 2, Bandung',
    'Jl. Diponegoro No. 3, Surabaya',
    'Jl. Gatot Subroto No. 4, Medan',
    'Jl. Malioboro No. 5, Yogyakarta',
    'Jl. Thamrin No. 6, Jakarta',
    'Jl. Asia Afrika No. 7, Bandung',
    'Jl. Pemuda No. 8, Surabaya',
    'Jl. Sisingamangaraja No. 9, Medan',
    'Jl. Solo No. 10, Yogyakarta',
    'Jl. Rasuna Said No. 11, Jakarta',
    'Jl. Braga No. 12, Bandung',
    'Jl. Tunjungan No. 13, Surabaya',
    'Jl. Ahmad Yani No. 14, Medan',
    'Jl. Parangtritis No. 15, Yogyakarta',
    'Jl. Kuningan No. 16, Jakarta',
    'Jl. Cihampelas No. 17, Bandung',
    'Jl. Basuki Rahmat No. 18, Surabaya',
    'Jl. Iskandar Muda No. 19, Medan',
    'Jl. Prawirotaman No. 20, Yogyakarta'
]
jenis_kelamin = ['Laki-laki', 'Laki-laki', 'Perempuan', 'Laki-laki', 'Laki-laki', 'Perempuan', 'Laki-laki', 'Laki-laki', 'Perempuan', 'Perempuan', 'Perempuan', 'Perempuan', 'Laki-laki', 'Laki-laki', 'Perempuan', 'Perempuan', 'Perempuan', 'Laki-laki', 'Laki-laki', 'Perempuan']
status_kelulusan = ['LULUS' if nilai >= 75 else 'TIDAK LULUS' for nilai in nilai_siswa]


# Fungsi untuk menampilkan data dalam bentuk tabel
def tampilkan_data():
    data = zip(no_id, nama_siswa, nilai_siswa, kelas_siswa, umur_siswa, alamat_siswa, jenis_kelamin, status_kelulusan)
    print(tabulate(data, headers=["ID", "Nama", "Nilai", "Kelas", "Umur", "Alamat", "Jenis Kelamin", "Status Kelulusan"], tablefmt="pipe"))
    print("\n\n")

# Fungsi untuk menambah data siswa
def tambah_data():
    global no_id
    while True:
        try:
            nama = input("Masukkan nama siswa (atau ketik 'batal' untuk kembali ke menu utama): ")
            if nama.lower() == 'batal':
                print(Fore.YELLOW + "Proses dibatalkan. Kembali ke menu utama.\n\n" + Style.RESET_ALL)
                return
            if not nama.replace(" ", "").isalpha() or len(nama) > 50:
                raise ValueError(Fore.RED + "Data yang anda masukkan tidak sesuai. Silakan masukkan huruf yang benar.\n\n" + Style.RESET_ALL)
            print(Fore.GREEN + "Nama berhasil dimasukkan.\n\n" + Style.RESET_ALL)
            
            while True:
                try:
                    nilai = input("Masukkan nilai siswa (atau ketik 'batal' untuk kembali ke menu utama): ")
                    if nilai.lower() == 'batal':
                        print(Fore.YELLOW + "Proses dibatalkan. Kembali ke menu utama.\n\n" + Style.RESET_ALL)
                        return
                    nilai = int(nilai)
                    if nilai < 1 or nilai > 100:
                        print(Fore.RED + "Nilai harus antara 1 dan 100. Silakan masukkan nilai yang benar.\n\n" + Style.RESET_ALL)
                        continue
                    print(Fore.GREEN + "Nilai berhasil dimasukkan.\n\n" + Style.RESET_ALL)
                    break
                except ValueError:
                    print(Fore.RED + "Nilai harus antara 1 dan 100. Silakan masukkan nilai yang benar.\n\n" + Style.RESET_ALL)
            
            while True:
                kelas = input("Masukkan kelas siswa (atau ketik 'batal' untuk kembali ke menu utama): ")
                if kelas.lower() == 'batal':
                    print(Fore.YELLOW + "Proses dibatalkan. Kembali ke menu utama.\n\n" + Style.RESET_ALL)
                    return
                if not any(char.isdigit() for char in kelas) or not any(char.isalpha() for char in kelas):
                    print(Fore.RED + "Data yang anda masukkan tidak sesuai. Silakan masukkan kelas yang mengandung angka dan huruf.\n\n" + Style.RESET_ALL)
                else:
                    angka = ''.join(filter(str.isdigit, kelas))
                    huruf = ''.join(filter(str.isalpha, kelas)).lower()
                    if angka.isdigit() and 1 <= int(angka) <= 12 and huruf in "abcdef" and len(huruf) == 1:
                        print(Fore.GREEN + "Kelas berhasil dimasukkan.\n\n" + Style.RESET_ALL)
                        break
                    else:
                        print(Fore.RED + "Kelas harus mengandung angka 1-12 dan huruf a-f. Silakan masukkan kelas yang benar.\n\n" + Style.RESET_ALL)
            
            while True:
                umur = input("Masukkan umur siswa (atau ketik 'batal' untuk kembali ke menu utama): ")
                if umur.lower() == 'batal':
                    print(Fore.YELLOW + "Proses dibatalkan. Kembali ke menu utama.\n\n" + Style.RESET_ALL)
                    return
                try:
                    umur = int(umur)
                    print(Fore.GREEN + "Umur berhasil dimasukkan.\n\n" + Style.RESET_ALL)
                    break
                except ValueError:
                    print(Fore.RED + "Data yang anda masukkan tidak sesuai. Silakan masukkan angka yang benar.\n\n" + Style.RESET_ALL)
            
            while True:
                alamat = input("Masukkan alamat siswa (atau ketik 'batal' untuk kembali ke menu utama): ")
                if alamat.lower() == 'batal':
                    print(Fore.YELLOW + "Proses dibatalkan. Kembali ke menu utama.\n\n" + Style.RESET_ALL)
                    return
                if len(alamat) > 100:
                    print(Fore.RED + "Alamat terlalu panjang. Silakan masukkan alamat yang lebih pendek.\n\n" + Style.RESET_ALL)
                else:
                    print(Fore.GREEN + "Alamat berhasil dimasukkan.\n\n" + Style.RESET_ALL)
                    break
            
            while True:
                jenis = input("Masukkan jenis kelamin (Laki-laki/Perempuan) (atau ketik 'batal' untuk kembali ke menu utama): ")
                if jenis.lower() == 'batal':
                    print(Fore.YELLOW + "Proses dibatalkan. Kembali ke menu utama.\n\n" + Style.RESET_ALL)
                    return
                if jenis.lower() not in ["laki-laki", "perempuan"]:
                    print(Fore.RED + "Data yang anda masukkan tidak sesuai. Silakan masukkan jenis kelamin Laki-laki atau Perempuan.\n\n" + Style.RESET_ALL)
                else:
                    print(Fore.GREEN + "Jenis kelamin berhasil dimasukkan.\n\n" + Style.RESET_ALL)
                    break
            
            no_id.append(str(int(no_id[-1]) + 1).zfill(5))
            nama_siswa.append(nama)
            nilai_siswa.append(nilai)
            kelas_siswa.append(kelas)
            umur_siswa.append(umur)
            alamat_siswa.append(alamat)
            jenis_kelamin.append(jenis.capitalize())
            status_kelulusan.append('LULUS' if nilai >= 75 else 'TIDAK LULUS')
            print(Fore.GREEN + "Data berhasil ditambahkan.\n\n" + Style.RESET_ALL)
            break
        except ValueError as e:
            print(e)

# Fungsi untuk menghapus data siswa
def hapus_data():
    try:
        id_hapus = input("Masukkan ID siswa yang akan dihapus: ")
        if id_hapus in no_id:
            index = no_id.index(id_hapus)
            no_id.pop(index)
            nama_siswa.pop(index)
            nilai_siswa.pop(index)
            kelas_siswa.pop(index)
            umur_siswa.pop(index)
            alamat_siswa.pop(index)
            jenis_kelamin.pop(index)
            status_kelulusan.pop(index)
            print(Fore.GREEN + "Data berhasil dihapus.\n\n" + Style.RESET_ALL)
        else:
            print(Fore.RED + "ID tidak ditemukan.\n\n" + Style.RESET_ALL)
    except ValueError as e:
        print(Fore.RED + str(e) + Style.RESET_ALL)

# Fungsi untuk memperbarui data siswa
def perbarui_data():
    while True:
        try:
            id_update = input("Masukkan ID siswa yang akan diperbarui: ")
            if id_update in no_id:
                index = no_id.index(id_update)
                
                while True:
                    nama = input("Masukkan nama baru (kosongkan jika tidak ingin mengubah): ")
                    if nama:
                        if not nama.replace(" ", "").isalpha() or len(nama) > 50:
                            print(Fore.RED + "Data yang anda masukkan tidak sesuai. Silakan masukkan huruf yang benar.\n\n" + Style.RESET_ALL)
                            continue
                        nama_siswa[index] = nama
                        print(Fore.GREEN + "Nama berhasil dimasukkan.\n\n" + Style.RESET_ALL)
                    break

                while True:
                    nilai = input("Masukkan nilai baru (kosongkan jika tidak ingin mengubah): ")
                    if nilai:
                        try:
                            nilai_siswa[index] = int(nilai)
                            status_kelulusan[index] = 'LULUS' if int(nilai) >= 75 else 'TIDAK LULUS'
                            print(Fore.GREEN + "Nilai berhasil dimasukkan.\n\n" + Style.RESET_ALL)
                        except ValueError:
                            print(Fore.RED + "Nilai harus antara 1 dan 100. Silakan masukkan nilai yang benar.\n\n" + Style.RESET_ALL)
                            continue
                    break

                while True:
                    kelas = input("Masukkan kelas baru (kosongkan jika tidak ingin mengubah): ")
                    if kelas:
                        if not any(char.isdigit() for char in kelas) or not any(char.isalpha() for char in kelas):
                            print(Fore.RED + "Data yang anda masukkan tidak sesuai. Silakan masukkan kelas yang mengandung angka dan huruf.\n\n" + Style.RESET_ALL)
                            continue
                        angka = ''.join(filter(str.isdigit, kelas))
                        huruf = ''.join(filter(str.isalpha, kelas)).upper()
                        if angka.isdigit() and 1 <= int(angka) <= 12 and huruf in "ABCDEF" and len(huruf) == 1:
                            kelas_siswa[index] = kelas
                            print(Fore.GREEN + "Kelas berhasil dimasukkan.\n\n" + Style.RESET_ALL)
                            break
                        else:
                            print(Fore.RED + "Kelas harus mengandung angka 1-12 dan satu huruf a-f. Silakan masukkan kelas yang benar.\n\n" + Style.RESET_ALL)
                    else:
                        break

                while True:
                    umur = input("Masukkan umur baru (kosongkan jika tidak ingin mengubah): ")
                    if umur:
                        try:
                            umur_siswa[index] = int(umur)
                            print(Fore.GREEN + "Umur berhasil dimasukkan.\n\n" + Style.RESET_ALL)
                        except ValueError:
                            print(Fore.RED + "Data yang anda masukkan tidak sesuai. Silakan masukkan angka yang benar.\n\n" + Style.RESET_ALL)
                            continue
                    break

                while True:
                    alamat = input("Masukkan alamat baru (kosongkan jika tidak ingin mengubah): ")
                    if alamat:
                        if len(alamat) > 100:
                            print(Fore.RED + "Alamat terlalu panjang. Silakan masukkan alamat yang lebih pendek.\n\n" + Style.RESET_ALL)
                            continue
                        alamat_siswa[index] = alamat
                        print(Fore.GREEN + "Alamat berhasil dimasukkan.\n\n" + Style.RESET_ALL)
                    break

                while True:
                    jenis = input("Masukkan jenis kelamin baru (kosongkan jika tidak ingin mengubah): ")
                    if jenis:
                        if jenis.lower() not in ["laki-laki", "perempuan"]:
                            print(Fore.RED + "Data yang anda masukkan tidak sesuai. Silakan masukkan jenis kelamin Laki-laki atau Perempuan.\n\n" + Style.RESET_ALL)
                            continue
                        jenis_kelamin[index] = jenis.capitalize()
                        print(Fore.GREEN + "Jenis kelamin berhasil dimasukkan.\n\n" + Style.RESET_ALL)
                    break

                print(Fore.GREEN + "Data berhasil diperbarui.\n\n" + Style.RESET_ALL)
                break
            else:
                print(Fore.RED + "ID tidak ditemukan.\n\n" + Style.RESET_ALL)
        except ValueError as e:
            print(e)


# Fungsi untuk memfilter data siswa berdasarkan status kelulusan
def filter_data():
    status = input("Masukkan status kelulusan (Lulus/Tidak Lulus): ").upper()
    if status not in ["LULUS", "TIDAK LULUS"]:
        print("Status kelulusan tidak valid.")
        return
    data = [(no_id[i], nama_siswa[i], nilai_siswa[i], kelas_siswa[i], umur_siswa[i], alamat_siswa[i], jenis_kelamin[i], status_kelulusan[i]) 
            for i in range(len(no_id)) if status_kelulusan[i].upper() == status]
    print(tabulate(data, headers=["ID", "Nama", "Nilai", "Kelas", "Umur", "Alamat", "Jenis Kelamin", "Status Kelulusan"], tablefmt="simple"))
    print("\n\n")

# Fungsi untuk melihat nilai tertinggi, terendah, dan rata-rata
def lihat_nilai():
    nilai_tertinggi = max(nilai_siswa)
    nilai_terendah = min(nilai_siswa)
    nilai_rata_rata = sum(nilai_siswa) / len(nilai_siswa)
    
    index_tertinggi = nilai_siswa.index(nilai_tertinggi)
    index_terendah = nilai_siswa.index(nilai_terendah)
    
    data_tertinggi = [
        ["ID", no_id[index_tertinggi]],
        ["Nama", nama_siswa[index_tertinggi]],
        ["Nilai", nilai_siswa[index_tertinggi]],
        ["Kelas", kelas_siswa[index_tertinggi]],
        ["Umur", umur_siswa[index_tertinggi]],
        ["Alamat", alamat_siswa[index_tertinggi]],
        ["Jenis Kelamin", jenis_kelamin[index_tertinggi]],
        ["Status Kelulusan", status_kelulusan[index_tertinggi]]
    ]
    
    data_terendah = [
        ["ID", no_id[index_terendah]],
        ["Nama", nama_siswa[index_terendah]],
        ["Nilai", nilai_siswa[index_terendah]],
        ["Kelas", kelas_siswa[index_terendah]],
        ["Umur", umur_siswa[index_terendah]],
        ["Alamat", alamat_siswa[index_terendah]],
        ["Jenis Kelamin", jenis_kelamin[index_terendah]],
        ["Status Kelulusan", status_kelulusan[index_terendah]]
    ]
    
    print("Data Siswa dengan Nilai Tertinggi:")
    print(tabulate(data_tertinggi, tablefmt="pipe"))
    print("\n")
    print("\nData Siswa dengan Nilai Terendah:")
    print(tabulate(data_terendah, tablefmt="pipe"))
    print("\n")
    print("\nNilai Rata-rata Siswa: {:.2f}".format(nilai_rata_rata))
    print("\n\n")




# Fungsi untuk menampilkan menu utama
def menu_utama():
    while True:
        print(Fore.BLUE + "=============================================================================="+ Style.RESET_ALL)
        print(Fore.YELLOW + Style.BRIGHT + pyfiglet.figlet_format("SISTEM INFORMASI DATA NILAI SISWA", font="standard") + Style.RESET_ALL)
        print(Fore.BLUE + "==============================================================================" + Style.RESET_ALL)
        print(Style.BRIGHT + "MENU UTAMA:" + Style.RESET_ALL)
        print(Fore.GREEN + "1. Melihat data Siswa")
        print("2. Menambah data siswa")
        print("3. Menghapus data siswa")
        print("4. Memperbarui data siswa")
        print("5. Filter data siswa berdasarkan status kelulusan")
        print("6. Melihat nilai siswa (tertinggi, terendah, rata-rata)")
        print("7. Exit Program"+ Style.RESET_ALL)
        pilihan = input("Pilih menu (1-7): ")
        print("\n")
        if pilihan == '1':
            tampilkan_data()
        elif pilihan == '2':
            tambah_data()
        elif pilihan == '3':
            hapus_data()
        elif pilihan == '4':
            perbarui_data()
        elif pilihan == '5':
            filter_data()
        elif pilihan == '6':
            lihat_nilai()
        elif pilihan == '7':
            print(Fore.GREEN + "Terima kasih telah menggunakan program ini.\n\n" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi.\n\n"+ Style.RESET_ALL)

# Fungsi untuk login
def login():
    while True:
        password = pwinput.pwinput(prompt="Masukkan password: ", mask='$') # fitur untuk masking password login
        if password == "Admin123":
            print(Fore.GREEN + "Login berhasil. Selamat datang!\n\n" + Style.RESET_ALL)
            menu_utama()
            break
        else:
            print(Fore.RED + "Password salah. Silakan coba lagi.\n\n" + Style.RESET_ALL)

# Memulai program dengan login
login()
