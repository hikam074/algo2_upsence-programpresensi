import csv                              # import csv
import os                               # agar bisa clean terminal
import pandas as pd                     # import pandas
import numpy as np                      # import numpy
from pathlib import Path                # import modul path
import tabulate                         # import nice table
import time                             # import time for counting time
import datetime                         # import time and date
from datetimerange import DateTimeRange # import range waktu
from datetime import timedelta          # melakukan operasi matematika pada objek datetime
import calendar                         # import kalender untuk melakukan operasi kalender

# HALAMAN LOGIN DAN LAUNCH PAGE ------------------------------------------------------------------------------------------------------------------------------
def launchPage():

    # WELCOME PAGE
    os.system('cls')
    print(logoLaunch,"\n")        # UI LOGO FOR WELCOME PAGE
    for i in range(delayWelcome,0,-1): 
        print("Meluncurkan program dalam :",i) 
        time.sleep(1)

    launch_page_condition = True    # LOOPING MENU AWAL (LAUNCH&LOGIN)
    while launch_page_condition:

        # LAUNCH PAGE
        os.system('cls')
        print(logoBorder)           # UI LOGO FOR LAUNCH PAGE
        print(launchInterface)      # UI LAUNCH PAGE
        launch_menu = input("Tekan [enter] untuk login, tekan [Q] untuk keluar program : ")     # MENU UMUM, UNTUK MASUK ATAU KELUAR DARI PROGRAM
        
        # MENU LOGIN
        if launch_menu == '':

            os.system('cls')
            print(logoBorder)       # UI LOGO FOR LOGIN PAGE
            print(loginInterface)   # UI LOGIN PAGE

            # MEMASUKKAN ID
            global launch_ID
            launch_ID = input("\nMasukkan ID anda : ")

            # MEMASUKKAN PASSCODE
            global launchPass
            launchPass = input("Masukkan Passcode anda : ")

            # MEMBUKA .CSV ADMIN DAN KARYAWAN
            with open('admin_account_database.csv','r') as fileAdmincsv:    # MEMBUKA .CSV ADMIN
                admin_list = fileAdmincsv.read()
            with open('employee_account_database.csv', 'r') as fileEmployeecsv: # MEMBUKA .CSV KARYAWAN
                employee_list = fileEmployeecsv.read()   

            # IDENTIFIKASI APAKAH MERUPAKAN AKUN ADMIN
            if launch_ID in admin_list:     # APAKAH ID DARI LOGIN ADA DI DATABASE ADMIN

                data_admin = []     # VARIABEL KOSONG UNTUK MENYIMPAN DATA ADMIN
                with open('admin_account_database.csv') as csvfile_admin:   # MEMBUKA .CSV ADMIN
                    reader_Admin = csv.reader(csvfile_admin)
                    for row in reader_Admin:    # menjadikan file .csv menjadi list admin (menambahkan tiap baris pada .csv kedalam variabel data admin)
                        data_admin.append(row)

                admin_column = [x[0] for x in data_admin]   # memecah data besar menjadi list-list data admin (menjadikan tiap data di list admin menjadi list-list terpisah)

                # MENGAUTENTIFIKASI ID DAN PASSCODE YANG DIMASUKKAN SESUAI ATAU TIDAK
                if launch_ID in admin_column:   # ID DAN PASSCODE ADA DI DATABASE ADMIN
                    for x in range(0,len(data_admin)):                                          # mencocokkan ID hasil login dengan ID di database
                        if launch_ID == data_admin[x][0] and launchPass == data_admin[x][4]:    # ID DAN PASSCODE SESUAI DENGAN DATABASE ADMIN
                            launch_page_condition = False
                            main_page_admin()                                                   # DIARAHKAN KE MENU ADMIN

                else:   # ID DAN/ATAU PASSCODE SALAH, LOOPING LAUNCH&LOGIN KEMBALI
                    input("\nPERHATIAN : ID atau Passcode salah, silahkan tekan [enter] untuk coba lagi")
                    launch_page_condition : True    # KEMBALI KE LAUNCH PAGE

            # IDENTIFIKASI APAKAH MERUPAKAN AKUN KARYAWAN
            elif launch_ID in employee_list:    # APAKAH ID DARI LOGIN ADA DI DATABASE KARYAWAN

                data_employee = []  # VARIABEL KOSONG UNTUK MENYIMPAN DATA KARYAWAN
                with open('employee_account_database.csv') as csvfile_employee: # MEMBUKA .CSV KARYAWAN
                    reader_employee = csv.reader(csvfile_employee)
                    for row in reader_employee:     # menjadikan file .csv menjadi list karyawan (menambahkan tiap baris pada .csv kedalam variabel data karyawan)
                        data_employee.append(row)

                employee_column = [x[0] for x in data_employee]     # memecah data besar menjadi list-list data karyawan (menjadikan tiap data di list karyawan menjadi list-list terpisah)

                # MENGAUTENTIFIKASI ID DAN PASSCODE YANG DIMASUKKAN SESUAI ATAU TIDAK
                if launch_ID in employee_column:    # ID DAN PASSCODE ADA DI DATABASE KARYAWAN
                    for x in range(0,len(data_employee)):
                        if launch_ID == data_employee[x][0] and launchPass == data_employee[x][6]:      # ID DAN PASSCODE SESUAI DENGAN DATABASE KARYAWAN
                            launch_page_condition = False
                            main_page_employee()                                                        # DIARAHKAN KE MENU KARYAWAN

                else:   # ID DAN/ATAU PASSCODE SALAH, LOOPING LAUNCH&LOGIN KEMBALI
                    input("\nPERHATIAN : ID atau Passcode salah, silahkan tekan [enter] untuk coba lagi")
                    launch_page_condition = True    # KEMBALI KE LAUNCH PAGE

            else:   # ID DAN PASSCODE TIDAK DITEMUKAN DI DATABASE MANAPUN
                input("\nPERHATIAN : ID atau Passcode tidak ditemukan, silahkan tekan [enter] untuk coba lagi")
                launch_page_condition = True    # KEMBALI KE LAUNCH PAGE

        # EXIT DAN MENUTUP PROGRAM
        elif launch_menu in 'Qq':   

            os.system('cls')
            time.sleep(0.5)
            print(logoLaunch, "\nTerimakasih telah memakai program ini\n\nMenutup program ...")
            time.sleep(1)
            print("Done")
            time.sleep(0.5)
            print("\n\n©Kelompok 2 Tugas Akhir Algo 1\n2023\n\n")     # UI LOGO UNTUK DAN CLOSING PAGE
            time.sleep(0.5)
            launch_page_condition = False   # MENGENTIKAN LOOPING LAUNCH&LOGIN
            break   # SELURH PROGRAM DIHENTIKAN
        
        # INPUT YANG DIMASUKKAN SALAH
        else:
            launch_page_condition = True    # KEMBALI KE LAUNCH PAGE

# LAUNCH PAGE SELESAI - UI : COMMENT : DESAIN

# ------------------------------------------------------------------------------------------------------------------------------------------------------------


# HALAMAN UTAMA ADMIN ----------------------------------------------------------------------------------------------------------------------------------------

def main_page_admin():
    os.system('cls')
    print(f'++{'='*86}++\n|| admin>menu utama>{' '*68}||\n++{'-'*86}++\n||{' '*86}||\n||{' '*27}M E N U   U T A M A   A D M I N{' '*28}||\n||{' '*86}||\n++{'='*86}++\nWaktu : {datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n')    # mengucapkan selamat datang

    # MENGIMPOR DATA ADMIN
    data_admin = []     # VARIABEL KOSONG UNTUK MENYIMPAN DATA ADMIN
    with open('admin_account_database.csv') as csvfile_admin:       # MEMBUKA .CSV ADMIN
        reader_Admin = csv.reader(csvfile_admin)
        for row in reader_Admin:        # menjadikan file .csv menjadi list admin (menambahkan tiap baris pada .csv kedalam variabel data admin)
            data_admin.append(row)

    admin_column = [x[0] for x in data_admin]   # memecah data besar menjadi list-list data admin (menjadikan tiap data di list admin menjadi list-list terpisah)

    # MENGIMPOR DATA KARYAWAN
    data_employee = []  # VARIABEL KOSONG UNTUK MENYIMPAN DATA KARYAWAN
    with open('employee_account_database.csv') as csvfile_employee: # MEMBUKA .CSV KARYAWAN
        reader_employee = csv.reader(csvfile_employee)
        for row in reader_employee:     # menjadikan file .csv menjadi list karyawan (menambahkan tiap baris pada .csv kedalam variabel data karyawan)
            data_employee.append(row)   

    employee_column = [y[0] for y in data_employee]     # memecah data besar menjadi list-list data karyawan (menjadikan tiap data di list karyawan menjadi list-list terpisah)

    # MENGIMPOR DATA PRESENSI
    data_presensi = []  # VARIABEL KOSONG UNTUK MENYIMPAN DATA PRESENSI
    with open('presensi_database.csv') as csvfile_presensi:     # MEMBUKA .CSV PRESENSI
        reader_presensi = csv.reader(csvfile_presensi)      # menjadikan file .csv menjadi list presensi (menambahkan tiap baris pada .csv kedalam variabel data presensi)
        for row in reader_presensi:
            data_presensi.append(row)

    # MENGIMPOR DATA HISTORI
    data_history = []  # VARIABEL KOSONG UNTUK MENYIMPAN DATA PRESENSI
    with open('histori_database.csv') as csvfile_histori:     # MEMBUKA .CSV PRESENSI
        reader_histori = csv.reader(csvfile_histori)      # menjadikan file .csv menjadi list presensi (menambahkan tiap baris pada .csv kedalam variabel data presensi)
        for row in reader_histori:
            data_history.append(row)

    histori_column = [y[0] for y in data_history]

    # MENDETEKSI NAMA ADMIN MENGGUNAKAN ID
    if launch_ID in admin_column:   # ID DAN PASSCODE ADA DI DATABASE ADMIN
        for x in range(0,len(data_admin)):      # mencocokkan ID hasil login dengan ID di database
            if launch_ID == data_admin[x][0]:   # ID DAN PASSCODE SESUAI DENGAN DATABASE ADMIN
                print(f'Selamat Datang, admin "{data_admin[x][1]}"!')   # selamat datang admin

    print('Apa yang ingin anda lakukan saat ini?\n\nMenu:\n[1] Tambahkan Orang\n[2] Edit Data\n[3] Edit Presensi Karyawan\n[4] Lihat Data\n[5] Hapus Data\n[6] KARYAWAN TERBAIK atau TERBURUK\n[7] Keluar\n\n[N] Notifkasi')    # pilihan menu admin
    menu_choice = input("\nPilih menu : ")
    print()

    if menu_choice == '1':          # FITUR 1 TAMBAHKAN ORANG
        menu_choice_1 = input("[1] Tambahkan Admin\n[2] Tambahkan Karyawan\nPilih menu : ")     # pilihan menambahkan admin/karyawan

        if menu_choice_1 == '1':    # FITUR 1.1 TAMBAHKAN ORANG>TAMBAHKAN ADMIN
            os.system('cls')
            print(f"++{'='*86}++\n|| {f"admin>menu utama>tambahkan orang>tambahkan admin>":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*28}T A M B A H K A N   A D M I N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n\n")  # UI TAMBAHKAN ADMIN
            masukkanAdminID = input("Masukkan ID admin : ")     # ID YANG HENDAK DITAMBAHKAN

            # MENDETEKSI APAKAH DATA ID SUDAH ADA
            if masukkanAdminID not in admin_column:     # BILA ID YANG HENDAK DITAMBAHKAN BELUM ADA
                masukkanAdminNama    = input("Masukkan nama admin : ")
                masukkanAdminPosisi  = input("Masukkan posisi admin : ")
                masukkanAdminBidang  = input("Masukkan bidang admin : ")
                masukkanAdminPass    = input("Masukkan passcode admin (case sensitive) : ")
                masukan_tambah_admin = [masukkanAdminID.upper(),masukkanAdminNama.upper(),masukkanAdminPosisi.upper(),masukkanAdminBidang.upper(),masukkanAdminPass]    # data yang akan ditambahkan
                
                data_admin.append(masukan_tambah_admin)     # Menambahkan data baru ke dalam list data admin
                
                with open('admin_account_database.csv', 'w', newline='') as csvfile_admin:      # Membuka file CSV dalam mode penulisan dan menulis data baru ke dalamnya
                    writer_admin = csv.writer(csvfile_admin)
                    writer_admin.writerows(data_admin)

                input(f'\nData baru : {masukkanAdminID.upper()},{masukkanAdminNama.upper()},{masukkanAdminPosisi.upper()},{masukkanAdminBidang.upper()},{masukkanAdminPass}\nPERHATIAN : Data admin berhasil ditambahkan!\n\nTekan [enter] untuk kembali ke menu utama')    # IN-PROGRAM-NOTIFIKASI BAHWA DATA ADMIN BARU BERHASIL DITAMBAHKAN

            else:       # BILA ID YANG HENDAK DITAMBAHKAN SUDAH ADA
                input(f'\nPERHATIAN : Data admin "{masukkanAdminID}" sudah ada!\n\nTekan [enter] untuk kembali ke menu utama')      # IN-PROGRAM-NOTIFIKASI BAHWA DATA ADMIN SUDAH ADA DI DATABASE ADMIN

            main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN

        # FITUR 1.1

        elif menu_choice_1 == '2':  # FITUR 1.2 TAMBAHKAN ORANG>TAMBAHKAN KARYAWAN
            os.system('cls')
            print(f"++{'='*86}++\n|| {f"admin>menu utama>tambahkan orang>tambahkan karyawan>":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*25}T A M B A H K A N   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n\n")    # UI TAMBAHKAN KARYAWAN

            # DEKLARASI SHIFT KASIR
            shiftPagiKasir  = [i for i in range(len(data_employee)) if ((data_employee[i][3] == 'True') and (data_employee[i][2] == 'KASIR'))]  # KASIR PAGI
            shiftSiangKasir = [i for i in range(len(data_employee)) if ((data_employee[i][4] == 'True') and (data_employee[i][2] == 'KASIR'))]  # KASIR SIANG
            shiftMalamKasir = [i for i in range(len(data_employee)) if ((data_employee[i][5] == 'True') and (data_employee[i][2] == 'KASIR'))]  # KASIR MALAM

            #DEKLARASI SHIFT STAF TOKO
            shiftPagiStaf  = [i for i in range(len(data_employee)) if (data_employee[i][3] == 'True' and (data_employee[i][2] == 'STAF TOKO'))] # STAF TOKO PAGI
            shiftSiangStaf = [i for i in range(len(data_employee)) if (data_employee[i][4] == 'True' and (data_employee[i][2] == 'STAF TOKO'))] # STAF TOKO SIANG
            shiftMalamStaf = [i for i in range(len(data_employee)) if (data_employee[i][5] == 'True' and (data_employee[i][2] == 'STAF TOKO'))] # STAF TOKO MALAM

            # DEKLARASI POSISI KASIR ATAU STAF
            shiftKasir = [i for i in range(len(data_employee)) if data_employee[i][2] == 'KASIR']
            shiftStaf = [i for i in range(len(data_employee)) if data_employee[i][2] == 'STAF TOKO']

            # ID KARYAWAN YANG HENDAK DITAMBAHKAN
            masukkanKaryawanID = input("Masukkan ID karyawan : ")

            # LOGIKA PENGARAH SHIFT (PAGI->SIANG->MALAM)--------------------------

            # ID KARYAWAN BELUM ADA DI DATABASE KARYAWAN
            if masukkanKaryawanID not in employee_column :  
                masukkanKaryawanNama = input("Masukkan nama karyawan : ") # MEMASUKKAN NAMA KARYAWAN

                ulangAdmin1_2Posisi = True  # LOOPING UNTUK MENU MASUKKAN DATA SELANJUTNYA
                while ulangAdmin1_2Posisi:

                    masukkanKaryawanPosisiNo = input("[1] Kasir [2] Staf Toko\nMasukkan posisi karyawan : ")    # MEMASUKKAN POSISI KARYAWAN : KASIR ATAU STAF

                    # MEMILIH KASIR
                    if masukkanKaryawanPosisiNo == '1':

                        # IDENTIFIKASI HANYA ADA 1 KASIR DALAM 1 SHIFT
                        if len(shiftKasir) < qKasir:   
                            ulangAdmin1_2Posisi = False
                            masukkanKaryawanPosisi = 'KASIR'

                            # APAKAH KASIR HENDAK DI SHIFT 1
                            masukkanKaryawanShift1 = input("\nMasukkan apakah karyawan bertugas Shift 1 (True/False) : ")
                            masukkanKaryawanShift1 = masukkanKaryawanShift1.lower()
                            # KASIR BISA DI SHIFT 1
                            if (masukkanKaryawanShift1.capitalize() == 'True' and len(shiftPagiKasir) < qKasirPagi):
                                    masukkanKaryawanShift1 = 'True'
                                    masukkanKaryawanShift2 = 'False'
                                    masukkanKaryawanShift3 = 'False'
                            # KASIR TIDAK BISA DI SHIFT 1
                            elif ((masukkanKaryawanShift1.capitalize() == 'True' and len(shiftPagiKasir) >= qKasirPagi)) or (masukkanKaryawanShift1.capitalize() == 'False'): 
                                input("Shift Pagi sudah penuh atau anda tidak memilih shift Pagi! plih shift yang lain...")
                                # APAKAH KASIR HENDAK DI SHIFT 2
                                masukkanKaryawanShift2 = input("Masukkan apakah karyawan bertugas Shift 2 (True/False) : ")
                                masukkanKaryawanShift2 = masukkanKaryawanShift2.lower()
                                # KASIR BISA DI SHIFT 2
                                if masukkanKaryawanShift2.capitalize() == 'True' and len(shiftSiangKasir) < qKasirSiang:
                                    masukkanKaryawanShift1 = 'False'
                                    masukkanKaryawanShift2 = 'True'
                                    masukkanKaryawanShift3 = 'False'
                                # KASIR TIDAK BISA DI SHIFT 2
                                elif (masukkanKaryawanShift2.capitalize() == 'True' and len(shiftSiangKasir) >= qKasirSiang) or (masukkanKaryawanShift2.capitalize() == 'False'):
                                    input("Shift Pagi dan Siang sudah penuh atau anda tidak memilih shift siang! mengarahkan ke Shift Malam...")
                                    # KASIR BISA DI SHIFT 3
                                    if len(shiftMalamKasir) < qKasirMalam:
                                        input("Kasir diarahkan ke shift malam!")
                                        masukkanKaryawanShift1 = 'False'
                                        masukkanKaryawanShift2 = 'False'
                                        masukkanKaryawanShift3 = 'True'
                                    # KASIR TIDAK BISA DI SHIFT 3
                                    elif len(shiftMalamKasir) >= qKasirMalam:
                                        input("Semua shift penuh! tidak dapat menambahkan data...\nTekan [enter] untuk kembali ke menu utama")
                                        main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN

                        # POSISI KASIR SUDAH PENUH
                        else:
                            print("\nPosisi untuk Kasir sudah penuh!Tidak bisa menambahkan data...\nTekan [enter] untuk kembali ke menu utama")
                            main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN

                    # MEMILIH STAF TOKO
                    elif masukkanKaryawanPosisiNo == '2':

                        # IDENTIFIKASI HANYA ADA 2 STAF PER 1 KASIR DALAM 1 SHIFT
                        if len(shiftStaf) < qStaf:
                            ulangAdmin1_2Posisi = False
                            masukkanKaryawanPosisi = 'STAF TOKO'

                            # APAKAH STAF HENDAK DI SHIFT 1
                            masukkanKaryawanShift1 = input("\nMasukkan apakah karyawan bertugas Shift 1 (True/False) : ")
                            masukkanKaryawanShift1 = masukkanKaryawanShift1.lower()
                            # STAF BISA DI SHIFT 1
                            if (masukkanKaryawanShift1.capitalize() == 'True' and len(shiftPagiStaf) < qStafPagi):
                                    masukkanKaryawanShift1 = 'True'
                                    masukkanKaryawanShift2 = 'False'
                                    masukkanKaryawanShift3 = 'False'
                            # STAF TIDAK BISA DI SHIFT 1
                            elif ((masukkanKaryawanShift1.capitalize() == 'True' and len(shiftPagiStaf) >= qStafPagi)) or (masukkanKaryawanShift1.capitalize() == 'False'): 
                                input("Shift Pagi sudah penuh atau anda tidak memilih shift Pagi! plih shift yang lain...")
                                # APAKAH STAF HENDAK DI SHIFT 2
                                masukkanKaryawanShift2 = input("Masukkan apakah karyawan bertugas Shift 2 (True/False) : ")
                                masukkanKaryawanShift2 = masukkanKaryawanShift2.lower()
                                # STAF BISA DI SHIFT 2
                                if masukkanKaryawanShift2.capitalize() == 'True' and len(shiftSiangStaf) < qStafSiang:
                                    masukkanKaryawanShift1 = 'False'
                                    masukkanKaryawanShift2 = 'True'
                                    masukkanKaryawanShift3 = 'False'
                                # STAF TIDAK BISA DI SHIFT 2
                                elif (masukkanKaryawanShift2.capitalize() == 'True' and len(shiftSiangStaf) >= qStafSiang) or (masukkanKaryawanShift2.capitalize() == 'False'):
                                    input("Shift Pagi dan Siang sudah penuh atau anda tidak memilih shift Siang! mengarahkan ke Shift Malam...")
                                    # STAF BISA DI SHIFT 3
                                    if len(shiftMalamStaf) < qStafMalam:
                                        input("Staf toko diarahkan ke shift malam!")
                                        masukkanKaryawanShift1 = 'False'
                                        masukkanKaryawanShift2 = 'False'
                                        masukkanKaryawanShift3 = 'True'
                                    # STAF TIDAK BISA DI SHIFT 3
                                    elif len(shiftMalamStaf) >= qStafMalam:
                                        print("Semua shift penuh! tidak dapat menambahkan data...\nTekan [enter] untuk kembali ke menu utama")
                                        main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN
                        
                        # POSISI STAF SUDAH PENUH
                        else:
                            print("\nPosisi untuk Staf Toko sudah penuh!Tidak bisa menambahkan data...\nTekan [enter] untuk kembali ke menu utama")
                            main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN
                    
                    # KESALAHAN INPUT (BUKAN KASIR ATAUPUN STAF)
                    else:
                        input("\nMasukan tidak valid, coba lagi...")
                        ulangAdmin1_2Posisi = True  # LOOPING MEMILIH POSISI KASIR ATAU STAF

                # INPUT PASSCODE KARYAWAN
                masukkanKaryawanPass = input("Masukkan passcode karyawan (case sensitive) : ")

                masukan_tambah_karyawan = [masukkanKaryawanID.upper(),masukkanKaryawanNama.upper(),masukkanKaryawanPosisi.upper(),masukkanKaryawanShift1.capitalize(),masukkanKaryawanShift2.capitalize(),masukkanKaryawanShift3.capitalize(),masukkanKaryawanPass] # DATA KARYAWAN BARU YANG AKAN DITAMBAHKAN
                
                # Menambahkan data baru ke dalam list data karyawan
                data_employee.append(masukan_tambah_karyawan)
                # Membuka file CSV dalam mode penulisan dan menulis data baru ke dalamnya
                with open('employee_account_database.csv', 'w', newline='') as csvfile_employee:
                    writer_employee = csv.writer(csvfile_employee)
                    writer_employee.writerows(data_employee)

                input(f'\nData baru : {masukkanKaryawanID.upper()},{masukkanKaryawanNama.upper()},{masukkanKaryawanPosisi.upper()},{masukkanKaryawanShift1.capitalize()},{masukkanKaryawanShift2.capitalize()},{masukkanKaryawanShift3.capitalize()},{masukkanKaryawanPass}\nPERHATIAN : Data karyawan berhasil ditambahkan!\n\nTekan [enter] untuk kembali ke menu utama') # IN-PROGRAM-NOTIFIKASI BAHWA DATA KARYAWAN BARU BERHASIL DITAMBAHKAN
            
            # ID KARYAWAN YANG HENDAK DITAMBAHKAN SUDAH ADA
            else:
                input(f'\nPERHATIAN : Data karyawan "{masukkanKaryawanID}" sudah ada!\n\nTekan [enter] untuk kembali ke menu utama')    # IN-PROGRAM-NOTIFIKASI BAHWA DATA KARYAWAN SUDAH ADA

            main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN

        # FITUR 1.2 

        else:                       # FITUR 1.3 BILA SALAH KEMBALI KE MENU UTAMA KARYAWAN
            main_page_admin()
        # FITUR 1.3 SELESAI - UI : COMMENT : DESAIN

    # FITUR 1 

    elif menu_choice == '2':        # FITUR 2 EDIT DATA 
        menu_choice_2 = input("[1] Edit Data Admin\n[2] Edit Data Karyawan\nPilih menu : ")     # pilihan mengedit data

        if menu_choice_2 == '1':    # FITUR 2.1 EDIT DATA>EDIT DATA ADMIN
            os.system('cls')
            df = pd.DataFrame(data_admin, columns=kolom_admin)  # MENGUBAH LIST MENJADI TABEL DENGAN PANDAS
            masukan_edit_admin = input(f"++{'='*86}++\n|| {f"admin>menu utama>edit data>edit data admin>":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*28}E D I T   D A T A   A D M I N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n\n\ndata saat ini:\n\n{tabulate.tabulate(df, headers="keys", tablefmt="github", showindex=False)}\n\nMasukkan ID admin yang hendak diubah : ")  # UI EDIT ADMIN

            # MENDETEKSI DATA ID YANG HENDAK DIUBAH ADA
            if masukan_edit_admin in df['ID'].values:   # BILA ID YANG HENDAK DIUBAH ITU ADA
                baris_admin = df[df['ID'] == masukan_edit_admin]  # Menemukan baris yang sesuai dengan ID
                print(f"\nData yang akan diedit : \n{baris_admin.to_string(index=False, header=False)}\nMasukkan [enter] untuk melewati pengeditan\n")  # KONFIRMASI DATA YANG HENDAK DIEDIT
                
                # MEMASUKKAN IDENTITAS BARU
                IDBaru     = input("Masukkan ID baru: ")
                namaBaru   = input("Masukkan nama baru: ")
                posisiBaru = input("Masukkan posisi baru: ")
                bidangBaru = input("Masukkan bidang baru: ")
                passBaru   = input("Masukkan passcode baru: ")

                # LOGIKA INPUTAN DATA BARU : BILA '' MAKA SKIP, BILA TIDAK MAKA AKAN DI-REPLACE

                # ID
                if IDBaru == '':    # SKIP
                    pass
                else:               # REPLACE
                    df.iloc[baris_admin.index, 0] = IDBaru.upper()
                # NAMA
                if namaBaru == '':  # SKIP
                    pass
                else:               # REPLACE
                    df.iloc[baris_admin.index, 1] = namaBaru.upper()
                # POSISI
                if posisiBaru == '':    #SKIP
                    pass
                else:                   # REPLACE
                    df.iloc[baris_admin.index, 2] = posisiBaru.upper()
                # BIDANG
                if bidangBaru == '':    # SKIP
                    pass
                else:                   # REPLACE
                    df.iloc[baris_admin.index, 3] = bidangBaru.upper()
                # PASSCODE
                if passBaru == '':  # SKIP
                    pass
                else:               # REPLACE
                    df.iloc[baris_admin.index, 4] = passBaru
                
                # MENYIMPAN DATA BARU KE DATABASE
                np.savetxt('admin_account_database.csv',df,delimiter=',',fmt='%s')

                print(f'\nData baru "{masukan_edit_admin}" telah diubah!\n\nData saat ini :\n{tabulate.tabulate(df, headers="keys", tablefmt="github", showindex=False)}\n')    # IN-PROGRAM-NOTIFICATION DATA BERHASIL DIUBAH

            else:   # DATA YANG HENDAK DIUBAH TIDAK ADA
                print(f'PERHATIAN : "{masukan_edit_admin}" tidak ada dalam database!')
            
            input("Tekan [enter] untuk kembali ke menu utama")
            main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN

        # FITUR 2.1 

        elif menu_choice_2 == '2':  # FITUR 2.2 EDIT DATA>EDIT DATA KARYAWAN
            os.system('cls')
            df = pd.DataFrame(data_employee, columns=kolom_employee)    # MENGUBAH LIST MENJADI TABEL DENGAN PANDAS
            masukan_edit_employee = input(f"++{'='*86}++\n|| {f"admin>menu utama>edit data>edit data karyawan>":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*25}E D I T   D A T A   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n\n\n\n{tabulate.tabulate(df, headers="keys", tablefmt="github", showindex=False)}\n\nMasukkan ID karyawan yang hendak diubah : ")  # UI EDIT KARYAWAN
            
            # MENDETEKSI DATA ID YANG HENDAK DIUBAH ADA
            if masukan_edit_employee in df['ID'].values:    # BILA ID YANG HENDAK DIUBAH ITU ADA
                baris_employee = df[df['ID'] == masukan_edit_employee]  # Menemukan baris yang sesuai dengan ID
                edit_employee_profil = input(f"\nData yang akan diedit : \n{baris_employee.to_string(index=False, header=False)}\n\nPilih [1] untuk mengedit data profil karyawan atau [2] untuk mengubah shift karyawan : ")   # KONFIRMASI DATA YANG HENDAK DIEDIT, PILIHAN MENGUBAH SHIFT ATAU DATA PROFIL
                print("Masukkan [enter] untuk melewati pengeditan\n")
                if edit_employee_profil == '1':     # FITUR 2.2.1 EDIT DATA>EDIT DATA KARYAWAN>EDIT DATA PROFIL
                    
                    # MEMASUKKAN IDENTITAS BARU
                    IDBaru     = input("Masukkan ID baru: ")
                    namaBaru   = input("Masukkan nama baru: ")
                    posisiBaru = input("Masukkan posisi baru: ")
                    passBaru   = input("Masukkan passcode baru: ")

                    # LOGIKA INPUTAN DATA BARU : BILA '' MAKA SKIP, BILA TIDAK MAKA AKAN DI-REPLACE

                    # ID
                    if IDBaru == '':    # SKIP
                        pass
                    else:               # REPLACE
                        df.iloc[baris_employee.index, 0] = IDBaru.upper()
                    # NAMA
                    if namaBaru == '':  # SKIP
                        pass
                    else:               # REPLACE
                        df.iloc[baris_employee.index, 1] = namaBaru.upper()
                    # POSISI
                    if posisiBaru == '':    # SKIP
                        pass
                    else:                   # REPLACE
                        df.iloc[baris_employee.index, 2] = posisiBaru.upper()
                    # PASSCODE
                    if passBaru == '':  # SKIP
                        pass
                    else:               # REPLACE
                        df.iloc[baris_employee.index, 6] = passBaru
                    
                    # MENYIMPAN DATA BARU KE DATABASE
                    np.savetxt('employee_account_database.csv',df,delimiter=',',fmt='%s')

                    print(f'\nData baru untuk "{df.iloc[baris_employee.index, 0:3].to_string(header=False,index=False)}" telah diubah!\n\nData saat ini :\n{tabulate.tabulate(df, headers="keys", tablefmt="github", showindex=False)}\n')  # IN-PROGRAM-NOTIFICATION DATA BERHASIL DIUBAH
                    input()

                # FITUR 2.2.1 

                elif edit_employee_profil == '2':   # FITUR 2.2.2 EDIT DATA>EDIT DATA KARYAWAN>EDIT DATA SHIFT
                    
                    # MEMASUKKAN SHIFT BARU (di .lower() agar tidak error saat kedepannya dipanggil)
                    shift1Baru = input("Masukkan shift 1 baru: ")
                    shift1Baru = shift1Baru.lower()
                    shift2Baru = input("Masukkan shift 2 baru: ")
                    shift2Baru = shift2Baru.lower()
                    shift3Baru = input("Masukkan shift 3 baru: ")
                    shift2Baru = shift2Baru.lower()

                    # LOGIKA INPUTAN DATA BARU : BILA '' MAKA SKIP, BILA TIDAK MAKA AKAN DI-REPLACE

                    # SHIFT 1
                    if shift1Baru == '':    # SKIP
                        pass
                    else:                   # REPLACE
                        df.iloc[baris_employee.index, 3] = shift1Baru.capitalize()
                    # SHIFT 2
                    if shift2Baru == '':    # SKIP
                        pass
                    else:                   # REPLACE
                        df.iloc[baris_employee.index, 4] = shift2Baru.capitalize()
                    # SHIFT 3
                    if shift3Baru == '':    # SKIP
                        pass
                    else:                   # REPLACE
                        df.iloc[baris_employee.index, 5] = shift3Baru.capitalize()
                    
                    # MENYIMPAN DATA BARU KE DATABASE
                    np.savetxt('employee_account_database.csv',df,delimiter=',',fmt='%s')

                    print(f'\nData baru untuk "{df.iloc[baris_employee.index, 0:3].to_string(header=False,index=False)}" telah diubah!\n\nData saat ini :\n{tabulate.tabulate(df, headers="keys", tablefmt="github", showindex=False)}\n')  # IN-PROGRAM-NOTIFICATION DATA BERHASIL DIUBAH
                    input()

                # FITUR 2.2.2 

                else:
                    input("kesalahan input, silahkan coba lagi")

    # FITUR 2.2

            else:    # DATA YANG HENDAK DIUBAH TIDAK ADA
                input("PERHATIAN : Kesalahan input atau data tidak ada...\nTekan [enter] untuk kembali ke menu utama")    

            main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN

        else:
            input("Tekan [enter] untuk kembali ke menu utama")
            main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN

    # FITUR 2

    elif menu_choice == '3':        # FITUR 3 EDIT DATA PRESENSI
        os.system('cls')
        df = pd.DataFrame(data_presensi, columns=kolom_presensi)    # MENGUBAH LIST MENJADI TABEL DENGAN PANDAS
        masukan_edit_presensi_id = input(F"++{'='*86}++\n|| {f"admin>menu utama>edit presensi karyawan>":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*21}E D I T   P R E S E N S I   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('\r%A, %d %B %Y | %H:%M:%S')}\n\n\n\nMasukkan ID karyawan yang hendak diubah : ")  # UI EDIT PRESENSI

        # MENDETEKSI DATA PRESENSI YANG HENDAK DIUBAH ITU ADA
        if masukan_edit_presensi_id in df['ID'].values:     # BILA DATA YANG HENDAK DIUBAH ITU ADA
            masukan_edit_presensi_tanggal = input("Masukkan tanggal yang dicari : ")    # MENCARI DATA YANG MEMILIKI ISI YANG SESUAI
            # FILTRASI DATA PANDAS YANG SESUAI DENGAN ID
            filtered_df = df.loc[df['ID'].str.contains(masukan_edit_presensi_id)]   # FILTRASI ID SESUAI
            filtered_df = filtered_df.loc[df['Tanggal'].str.contains(masukan_edit_presensi_tanggal)]    # FILTRASI TANGGAL SESUAI
            
            # BILA HASIL FILTRASI TIDAK ADA (DATA YANG DICARI TIDAK ADA)
            if len(filtered_df) == 0 :
                print("\nData yang anda cari tidak ditemukan...\n")
            
            # BILA HASIL FILTRASI ADA (DATA YANG DICARI ADA)
            else :
                print(f'\nHasil pencarian :\n\n{tabulate.tabulate(filtered_df, headers="keys", tablefmt="github")}')
                masukan_edit_presensi_index = int(input("\npilih index yang akan diedit: "))    # KONFIRMASI DATA PRESENSI YANG HENDAK DIEDIT

                # MENCOCOKKAN INDEX DATA YANG ADA DENGAN INDEX DATA YANG HENDAK DIEDIT
                if masukan_edit_presensi_index == filtered_df.index :
                    print(f"\nData yang akan diedit : \n{tabulate.tabulate((df[masukan_edit_presensi_index:masukan_edit_presensi_index+1]), headers="keys", tablefmt="github", showindex=False)}\n\nTekan [enter] untuk melewati perubahan\n")  # KONFIRMASI PENGEDITAN

                    # INPUTAN DATA
                    masukanEditPresensiTanggalBaru = input("Masukkan tanggal baru : ")  
                    masukanEditPresensiWaktuBaru   = input("Masukkan waktu baru : ")
                    masukanEditPresensiIDBaru      = input("Masukkan ID baru : ")
                    masukanEditPresensiNamaBaru    = input("Masukkan Nama baru : ") 
                    masukanEditPresensiShiftBaru   = input("Masukkan Shift baru : ")
                    masukanEditPresensiStatusBaru  = input("Masukkan Status kehadiran baru : ")

                    # LOGIKA INPUTAN DATA BARU : BILA '' MAKA SKIP, BILA TIDAK MAKA AKAN DI-REPLACE

                    # TANGGAL
                    if masukanEditPresensiTanggalBaru == '':# SKIP
                        pass
                    else:                                   # REPLACE
                        df.iloc[masukan_edit_presensi_index, 0] = masukanEditPresensiTanggalBaru.upper()
                    # WAKTU
                    if masukanEditPresensiWaktuBaru == '':  # SKIP
                        pass
                    else:                                   # REPLACE
                        df.iloc[masukan_edit_presensi_index, 5] = masukanEditPresensiWaktuBaru.upper()
                    # ID
                    if masukanEditPresensiIDBaru == '':     # SKIP
                        pass
                    else:                                   # REPLACE
                        df.iloc[masukan_edit_presensi_index, 1] = masukanEditPresensiIDBaru.upper()
                    # NAMA
                    if masukanEditPresensiNamaBaru == '':   # SKIP
                        pass
                    else:                                   # REPLACE
                        df.iloc[masukan_edit_presensi_index, 2] = masukanEditPresensiNamaBaru.upper()
                    # SHIFT
                    if masukanEditPresensiShiftBaru == '':  # SKIP
                        pass
                    else:                                   # REPLACE
                        df.iloc[masukan_edit_presensi_index, 3] = masukanEditPresensiShiftBaru.upper()
                    # STATUS KEHADIRAN
                    if masukanEditPresensiStatusBaru == '': #SKIP
                        pass
                    else:                                   # REPLACE
                        df.iloc[masukan_edit_presensi_index, 4] = masukanEditPresensiStatusBaru.upper()
                    
                    # MENYIMPAN DATA BARU KE DATABASE
                    np.savetxt('presensi_database.csv',df,delimiter=',',fmt='%s')
                    print(f'\nData baru "{masukan_edit_presensi_id}" telah diubah!\n\nData saat ini :\n{tabulate.tabulate((df[masukan_edit_presensi_index:masukan_edit_presensi_index+1]), headers="keys", tablefmt="github", showindex=False)}\n') # IN-PROGRAM-NOTIFICATION DATA BERHASIL DIUBAH
                
                # INDEX MASUKAN TIDAK COCOK DENGAN YANG HENDAK DIUBAH
                else:
                    print("Input anda tidak dalam range yang hendak diedit!\n")

        # DATA YANG HENDAK DIUBAH TIDAK ADA
        else:
            print(f"{masukan_edit_presensi_id} tidak ada dalam database.")
 
        input("Tekan [enter] untuk kembali ke menu utama")  # back to main menu
        main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN

    # FITUR 3

    elif menu_choice == '4':        # FITUR 4 LIHAT DATA
        menu_choice_4 = input("[1] Lihat Data Admin\n[2] Lihat Data Karyawan\n[3] Lihat Presensi Karyawan\n[enter] Kembali ke menu utama\n\nPilih menu : ")

        if menu_choice_4 == '1':    # FITUR 4.1 LIHAT DATA>LIHAT DATA ADMIN
            os.system('cls')
            print(f"++{'='*86}++\n|| {f"admin>menu utama>lihat data>lihat data admin>":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*27}L I H A T   D A T A   A D M I N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n\n\n")
            # MENAMPILKAN DATA
            df = pd.DataFrame(data_admin, columns=kolom_admin)
            print(tabulate.tabulate(df, headers="keys", tablefmt="grid", showindex=False))  
            # FITUR SEARCH BERDASARKAN ID
            search_ID = input("\nMasukkan ID yang hendak dicari : ")
            # MEMBUKA KEMBALI DATABASE UNTUK SEARCHING
            with open('admin_account_database.csv', 'r') as csvfile_admin:
                data_admin_s = csvfile_admin.readlines()
            df = pd.DataFrame([entry.strip().split(',') for entry in data_admin_s],columns=kolom_admin)
            # HASIL SEARCH
            if search_ID in df['ID'].values:    # SEARCHING ADA DI DATABASE  
                os.system('cls')
                print(f"++{'='*86}++\n|| {f"admin>menu utama>lihat data>lihat data admin>cari ID>":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*27}L I H A T   D A T A   A D M I N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n\n") 
                filtered_df = df.loc[df['ID'].str.contains(search_ID)]  # deklarasi data hasil filter
                print(f'\nHasil Pencarian untuk ID "{search_ID}"\n')    # memunculkan data di terminal
                print(tabulate.tabulate(filtered_df, headers='keys', tablefmt='grid', showindex=False))

            else:   # HASIL SEARCHING TIDAK DITEMUKAN
                print("\nData yang anda cari tidak ada...")
            
            input("\nTekan [enter] untuk kembali ke menu utama") 
            main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN

        # FITUR 4.1

        elif menu_choice_4 == '2':    # FITUR 4.2 LIHAT DATA>LIHAT DATA KARYAWAN
            os.system('cls')
            print(f"++{'='*86}++\n|| {f"admin>menu utama>lihat data>lihat data karyawan>":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*24}L I H A T   D A T A   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n\n\n\njadwal minggu ini\n")
            # MENAMPILKAN DATA
            # DISPLAY TABEL
            df = pd.DataFrame(data_employee, columns=kolom_employee)    # MEMASUKKAN LIST DATA BESAR KE PANDAS
            df['Shift 1'] = df["Shift 1"].str.replace('True','PAGI')    # MEMBUAT SHIFT 1 TAMPIL KARENA BENAR
            df['Shift 2'] = df["Shift 2"].str.replace('True','SIANG')   # MEMBUAT SHIFT 2 TAMPIL KARENA BENAR
            df['Shift 3'] = df["Shift 3"].str.replace('True','MALAM')   # MEMBUAT SHIFT 3 TAMPIL KARENA BENAR
            df['Shift 1'] = df["Shift 1"].str.replace('False','-')      # MEMBUAT SHIFT 1 SEMBUNYI KARENA SALAH
            df['Shift 2'] = df["Shift 2"].str.replace('False','-')      # MEMBUAT SHIFT 1 SEMBUNYI KARENA SALAH
            df['Shift 3'] = df["Shift 3"].str.replace('False','-')      # MEMBUAT SHIFT 1 SEMBUNYI KARENA SALAH
            print(tabulate.tabulate(df, headers="keys", tablefmt="grid", showindex=False))  # PRINT TABEL                                             # menampilkan data
            # FITUR SEARCH BERDASARKAN ID
            search_ID = input("\nMasukkan ID yang hendak dicari : ")
            # MEMBUKA KEMBALI DATABASE UNTUK SEARCHING
            with open('employee_account_database.csv', 'r') as csvfile_employee:
                data_employee = csvfile_employee.readlines()
            df = pd.DataFrame([entry.strip().split(',') for entry in data_employee],columns=kolom_employee)
            # HASIL SEARCH
            if search_ID in df['ID'].values:    # SEARCHING ADA DI DATABASE
                os.system('cls')
                print(f"++{'='*86}++\n|| {f"admin>menu utama>lihat data>lihat data karyawan>cari ID>":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*24}L I H A T   D A T A   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n\n") 
                filtered_df = df.loc[df['ID'].str.contains(search_ID)]  # deklarasi data hasil filter
                print(f'\nHasil Pencarian untuk ID "{search_ID}"\n')    # memunculkan data di terminal
                print(tabulate.tabulate(filtered_df, headers='keys', tablefmt='grid', showindex=False))

            else:   # HASIL SEARCHING TIDAK DITEMUKAN
                print("\nData yang anda cari tidak ada...")

            input("\nTekan [enter] untuk kembali ke menu utama")  # back to main menu
            main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN

        elif menu_choice_4 == '2':    # FITUR 4.2 LIHAT DATA>LIHAT DATA KARYAWAN
            os.system('cls')
            print(f"++{'='*86}++\n|| {f'admin>menu utama>lihat data>lihat data karyawan>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*24}L I H A T   D A T A   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('\r%A, %d %B %Y | %H:%M:%S')}\n\n\n\njadwal minggu ini\n")
                
            # MENAMPILKAN DATA
            # DISPLAY TABEL
            df = pd.DataFrame(data_employee, columns=kolom_employee)    # MEMASUKKAN LIST DATA BESAR KE PANDAS                df = df.sort_values(by="ID")  # Mengurutkan DataFrame berdasarkan ID

            # Menampilkan DataFrame dengan format tabel
            df['Shift 1'] = df["Shift 1"].str.replace('True', 'PAGI').replace('False', '-')
            df['Shift 2'] = df["Shift 2"].str.replace('True', 'SIANG').replace('False', '-')
            df['Shift 3'] = df["Shift 3"].str.replace('True', 'MALAM').replace('False', '-')
            print(tabulate.tabulate(df, headers="keys", tablefmt="grid", showindex=False))  # Menampilkan tabel
                
            # FITUR SEARCH BERDASARKAN ID
            search_ID = input("\nMasukkan ID yang hendak dicari: ")
                
            # Convert search_ID to the same data type as in the DataFrame
            search_ID = str(search_ID)
                
            # Inisialisasi variabel untuk binary search
            left, right = 0, len(df) - 1
            hasil_pencarian = None
                
            # Algoritma Binary Search
            while left <= right:
                mid = (left + right) // 2
                mid_id = df.iloc[mid]["ID"]
                if mid_id == search_ID:
                    hasil_pencarian = df.iloc[mid]
                    break
                elif mid_id < search_ID:
                    left = mid + 1
                else:
                    right = mid - 1               
                
                # Output hasil pencarian
            if hasil_pencarian is not None:
                print("Data Karyawan Ditemukan:")
                print(f"ID: {hasil_pencarian['ID']}")
                print(f"Nama: {hasil_pencarian['Nama']}")
                print(f"Posisi: {hasil_pencarian['Posisi']}")
            else:
                print("Karyawan dengan ID tersebut tidak ditemukan.")
                
            input("\nTekan [enter] untuk kembali ke menu utama")  # Kembali ke menu utama
            main_page_admin()  # MENGEMBALIKAN KE MENU UTAMA ADMIN    

        # FITUR 4.2 

        elif menu_choice_4 == '3':    # FITUR 4.3 LIHAT DATA>LIHAT PRESENSI KARYAWAN
            os.system('cls')
            print(f"++{'='*86}++\n|| {f'admin>menu utama>lihat data>lihat presensi karyawan>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*21}L I H A T   P R E S E N S I   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('\r%A, %d %B %Y | %H:%M:%S')}\n")

            # MENAMPILKAN DATA
            df = pd.DataFrame(data_presensi, columns=kolom_presensi)  # memasukkan data list ke pandas
            df = df.sort_values(by='ID', ascending=True)  # Sortir berdasarkan ID

            # FITUR SEARCH BERDASARKAN ID
            search_ID = input("\nMasukkan ID yang hendak dicari : ")

            # Implementasi Pencarian Biner
            left, right = 0, len(df) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                mid_id = df.iloc[mid]['ID']
                if mid_id == search_ID:
                    index = mid
                    break
                elif mid_id < search_ID:
                    left = mid + 1
                else:
                    right = mid - 1

            if index != -1:  # SEARCHING ADA DI DATABASE
                menu_presensi_karyawan = input("\n[1] Lihat Data Presensi\n[2] Lihat Rekapitulasi Presensi\nMasukan opsi : ")
                
                if menu_presensi_karyawan == '1':
                    os.system('cls')
                    print(f"++{'='*86}++\n|| {f'admin>menu utama>lihat data>lihat presensi karyawan>cari ID>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*21}L I H A T   P R E S E N S I   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('\r%A, %d %B %Y | %H:%M:%S')}\n\n")

                    filtered_df = df.iloc[[index]]  # deklarasi data hasil filter
                    print(f'\nHasil Pencarian untuk ID "{search_ID}"\n')
                    print(tabulate.tabulate(filtered_df, headers='keys', tablefmt='github', showindex=False))

                    # SEARCHING LAGI DENGAN TANGGAL
                    search_date = input("\nMasukkan Tanggal yang hendak dicari [yyyy-mm-dd] : ")

                    if search_date in filtered_df['Tanggal'].values:  # SEARCHING ADA DI DATABASE
                        os.system('cls')
                        print(f"++{'='*86}++\n|| {f'admin>menu utama>lihat data>lihat presensi karyawan>cari ID>cari tanggal>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*21}L I H A T   P R E S E N S I   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('\r%A, %d %B %Y | %H:%M:%S')}\n\n")

                        filtered_df = filtered_df.loc[filtered_df['Tanggal'].str.contains(search_date)]
                        print(f'\nHasil Pencarian untuk tanggal "{search_date}"\n')
                        print(tabulate.tabulate(filtered_df, headers='keys', tablefmt='github', showindex=False))
                    else:  # HASIL SEARCHING DENGAN TANGGAL TIDAK DITEMUKAN
                        print("\nData yang anda cari tidak ada...")

                # FITUR 4.3.2 LIHAT DATA>LIHAT REKAPITULASI PRESENSI KARYAWAN
                elif menu_presensi_karyawan == '2':
                    
                    # Filter DataFrame berdasarkan ID yang sudah login
                    filtered_df = df.loc[df['ID'] == search_ID]

                    # Pilihan untuk rekap mingguan atau bulanan
                    ulangAdmin4 = True
                    while ulangAdmin4:
                        rekap_choice = input("\nPilih jenis rekapitulasi\n[1] Minggu Ini\n[2] Minggu Lalu\n[3] Bulan Ini\n[4] Bulan Lalu\n[5] Kembali ke menu utama\n\nMasukkan pilihan : ")

                        now = datetime.datetime.now()

                        if rekap_choice == '1':  # Minggu Ini
                            rekap_choice_word = "minggu ini"
                            ulangAdmin4 = False
                            start_date = (now - timedelta(days=now.weekday())).strftime('%Y-%m-%d')
                            end_date = (now + timedelta(days=(6 - now.weekday()))).strftime('%Y-%m-%d')
                            total_days = 7

                        elif rekap_choice == '2':  # Minggu Lalu
                            rekap_choice_word = "minggu lalu"
                            ulangAdmin4 = False
                            start_date = (now - timedelta(days=(now.weekday() + 7))).strftime('%Y-%m-%d')
                            end_date = (now - timedelta(days=now.weekday() + 1)).strftime('%Y-%m-%d')
                            total_days = 7

                        elif rekap_choice == '3':  # Bulan Ini
                            rekap_choice_word = "bulan ini"
                            ulangAdmin4 = False
                            start_date = f'{now.year}-{now.month:02d}-01'
                            last_day = calendar.monthrange(now.year, now.month)[1]
                            end_date = f'{now.year}-{now.month:02d}-{last_day}'
                            total_days = last_day

                        elif rekap_choice == '4':  # Bulan Lalu
                            rekap_choice_word = "bulan lalu"
                            ulangAdmin4 = False
                            last_month = (now.replace(day=1) - timedelta(days=1)).replace(day=1)
                            start_date = f'{last_month.year}-{last_month.month:02d}-01'
                            last_day = calendar.monthrange(last_month.year, last_month.month)[1]
                            end_date = f'{last_month.year}-{last_month.month:02d}-{last_day}'
                            total_days = last_day

                        elif rekap_choice == '5':
                            input("\nTekan [enter] untuk kembali ke menu utama")
                            main_page_admin()    # MENGEMBALIKAN KE MENU UTAMA

                        else:
                            input('Pilihan yang anda berikan tidak ada!\nCoba lagi')    # KESALAHAN INPUT, KEMBALI KE NEMU REKAP
                            ulangAdmin4 = True
                    
                    # Filter DataFrame berdasarkan tanggal
                    filtered_df = filtered_df.loc[(filtered_df['Tanggal'] >= start_date) & (filtered_df['Tanggal'] <= end_date)]

                    # Menghitung statistik kehadiran
                    total_kehadiran_tepat_waktu = len(filtered_df[filtered_df['Kehadiran'].str.upper() == 'HADIR'])
                    total_terlambat = len(filtered_df[filtered_df['Kehadiran'].str.upper() == 'TERLAMBAT'])
                    total_kehadiran = total_kehadiran_tepat_waktu + total_terlambat
                    total_tidak_hadir = len(filtered_df[filtered_df['Kehadiran'].str.upper() == 'TIDAK HADIR'])

                    total_hari_kerja = total_kehadiran + total_tidak_hadir  # Total hari kerja dihitung berdasarkan jumlah data presensi

                    # Menampilkan statistik kehadiran
                    os.system('cls')
                    print(f'++{'='*86}++\n|| {'admin>menu utama>lihat data>lihat rekapitulasi presensi karyawan>'f"{rekap_choice_word}"'>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{' '*23}R E K A P I T U L A S I   P R E S E N S I{' '*22}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n\nMenampilkan rekapitulasi "{rekap_choice_word.upper()}"\n{start_date} | {end_date}\n\n\nTOTAL HADIR : {total_kehadiran}')  # UI HASIL REKAPAN

                    # Rincian Total Kehadiran
                    print("    Rincian:")
                    print(f"      -Total Hadir Tepat Waktu: {total_kehadiran_tepat_waktu}")
                    print(f"      -Total Terlambat: {total_terlambat}")

                    print(f"\nTOTAL TIDAK HADIR : {total_tidak_hadir}")

                    # Persentase Kehadiran
                    if total_hari_kerja > 0:
                        attendance_percentage = round((total_kehadiran / total_hari_kerja * 100))
                        print(f"\nPERSENTASE KEHADIRAN ({start_date} sampai {end_date}): {attendance_percentage}% ({total_kehadiran} dari {total_hari_kerja} hari kerja)")
                    else:
                        print("\nTidak ada data kehadiran pada periode yang dipilih.")

                    input("\n\n\nTekan [enter] untuk kembali ke Main Menu")
                    main_page_admin()    # MENGEMBALIKAN KE MENU UTAMA

            else:   # HASIL SEARCHING TIDAK DITEMUKAN
                print("\nData yang anda cari tidak ada...")

            input("\nTekan [enter] untuk kembali ke menu utama")
            main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN

        # FITUR 4.3

        else:   # BILA INPUTAN PILIHAN SALAH
            main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN

    # FITUR 4 SELESAI - UI : COMMENT : DESAIN

    elif menu_choice == '5':        # FITUR 5 HAPUS DATA
        menu_choice_5 = input("[1] Hapus Data Admin\n[2] Hapus Data Karyawan\n[3] Hapus Presensi Karyawan\nPilih menu : ")  # PILIHAN DATA MANA YANG HENDAK DIHAPUS

        if menu_choice_5 == '1':    # FITUR 5.1 HAPUS DATA>HAPUS DATA ADMIN
            os.system('cls')
            print(f"++{'='*86}++\n|| {f"admin>menu utama>hapus data>":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*27}H A P U S   D A T A   A D M I N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n\n\nmenampilkan keseluruhan data...\n") # UI HAPUS DATA
            df = pd.DataFrame(data_admin, columns=kolom_admin)  # MENGUBAH LIST MENJADI TABEL DENGAN PANDAS
            print(tabulate.tabulate(df, headers="keys", tablefmt="github", showindex=False))    # MENAMPILKAN TABEL KE TERMINAL

            # MENDETEKSI DATA YANG HENDAK DIHAPUS ITU ADA
            menghapus_file = input("\nMasukkan ID admin yang mau dihapus : ")      # user memasukkan data yang ingin dihapus
            # identifikasi data yang akan dihapus didapatkan dari  admin_column = [x[0] for x in data_admin]
            
            if menghapus_file in admin_column:  # BILA DATA YANG HENDAK DIHAPUS ITU ADA
                for x in range(0,len(data_admin)):  # mencari di seluruh database admin
                    # BILA DATA YANG DICOCOKKAN SAMA DENGAN YANG DICARI
                    if menghapus_file == data_admin[x][0]:  # DATA COCOK
                        print(f'Data admin yang akan dihapus : "{data_admin[x]}"!\n')   # KONFIRMASI DATA YANG HENDAK DIHAPUS
                        pilihan_admin_hapus = input("Anda yakin?\nTekan [1] untuk menghapus\nTekan [2] atau [tombol lain] untuk membatalkan : ")    # KONFIRMASI HENDAK MENGHAPUS ATAU TIDAK
                        # DATA JADI DIHAPUS
                        if pilihan_admin_hapus == '1':
                            df = pd.DataFrame(data_admin, columns=kolom_admin)                  # deklarasi tabel pandas
                            df = df.drop(x)                                                     # menghapus data yang diinginkan
                            np.savetxt('admin_account_database.csv',df,delimiter=',',fmt='% s') # meyimpan kembali data yang tidak dihapus
                            input(f"\nID terhapus : {menghapus_file}")  # IN-PROGRAM-NOTIFICATION DATA YANG TELAH DIHAPUS
                            print(f"Hasil data : \n{tabulate.tabulate(df, headers="keys", tablefmt="github", showindex=False)}")    # DATA TERSISA
                            input("\nTekan [enter] untuk kembali ke menu utama")
                            main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN
                        # DATA TIDAK JADI DIHAPUS
                        else:
                            input("\nMembatalkan ... Tekan [enter] untuk kembali ke menu utama")
                            main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN
                    else:   # DATA TIDAK COCOK
                        pass

            else:   # BILA DATA YANG HENDAK DIHAPUS TIDAK ADA
                input("\nData tidak ada ... Tekan [enter] untuk kembali ke menu utama")
                main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN

        # FITUR 5.1

        elif menu_choice_5 == '2':    # FITUR 5.2 HAPUS DATA>HAPUS DATA KARYAWAN

            os.system('cls')
            print(f"++{'='*86}++\n|| {f"admin>menu utama>hapus data>":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*24}H A P U S   D A T A   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n\n\nmenampilkan keseluruhan data...\n")  # UI HAPUS DATA
            df = pd.DataFrame(data_employee, columns=kolom_employee)    # MENGUBAH LIST MENJADI TABEL DENGAN PANDAS
            print(tabulate.tabulate(df, headers="keys", tablefmt="github", showindex=False))    # MENAMPILKAN TABEL KE TERMINAL

            # MENDETEKSI DATA YANG HENDAK DIHAPUS ITU ADA
            menghapus_file = input("\nMasukkan ID admin yang mau dihapus : ")      # user memasukkan data yang ingin dihapus
            # identifikasi data yang akan dihapus didapatkan dari  employee_column = [x[0] for x in data_employee]

            if menghapus_file in employee_column:   # BILA DATA YANG HENDAK DIHAPUS ITU ADA
                for x in range(0,len(data_employee)):   # mencari di seluruh database admin
                    # BILA DATA YANG DICOCOKKAN SAMA DENGAN YANG DICARI
                    if menghapus_file == data_employee[x][0]:   # DATA COCOK
                        print(f'Data karyawan yang akan dihapus : "{data_employee[x]}"!\n')# KONFIRMASI DATA YANG HENDAK DIHAPUS
                        pilihan_employee_hapus = input("Anda yakin?\nTekan [1] untuk menghapus\nTekan [2] atau [tombol lain] untuk membatalkan : ") # KONFIRMASI HENDAK MENGHAPUS ATAU TIDAK
                        # DATA JADI DIHAPUS
                        if pilihan_employee_hapus == '1':
                            df = pd.DataFrame(data_employee, columns=kolom_employee)                # deklarasi tabel pandas
                            df = df.drop(x)                                                         # menghapus data yang diinginkan
                            np.savetxt('employee_account_database.csv',df,delimiter=',',fmt='% s')  # meyimpan kembali data yang tidak dihapus
                            input(f"\nID dihapus : {menghapus_file}\n") # IN-PROGRAM-NOTIFICATION DATA YANG TELAH DIHAPUS
                            print(f"Hasil data : \n{tabulate.tabulate(df, headers="keys", tablefmt="github", showindex=False)}")    # DATA TERSISA
                            input("\nTekan [enter] untuk kembali ke menu utama")
                            main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN
                        # DATA TIDAK JADI DIHAPUS
                        else:
                            input("\nMembatalkan ... Tekan [enter] untuk kembali ke menu utama")
                            main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN
                    else:   # DATA TIDAK COCOK
                        pass

            else:   # BILA DATA YANG HENDAK DIHAPUS TIDAK ADA
                input("\nData tidak ada ... Tekan [enter] untuk kembali ke menu utama")
                main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN

        # FITUR 5.2 

        elif menu_choice_5 == '3':    # FITUR 5.3 HAPUS PRESENSI KARYAWAN
            os.system('cls')
            print(f"++{'='*86}++\n|| {f"admin>menu utama>hapus presensi karyawan>":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*21}H A P U S   P R E S E N S I   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n\n=\n\n") # UI HAPUS DATA
            df = pd.DataFrame(data_presensi, columns=kolom_presensi)    # MENGUBAH LIST MENJADI TABEL DENGAN PANDAS
            
            # MENCARI TANGGAL YANG HENDAK DIHAPUS ITU ADA
            masukkan_tanggal_presensi = str(input("\nMasukkan tanggal yang dicari : "))  # user memasukkan data yang ingin dihapus
            print()
            # FILTRASI TANGGAL YANG SESUAI DENGAN YANG DICARI
            filtered_df = df.loc[df['Tanggal'].str.contains(masukkan_tanggal_presensi)]        
            print(tabulate.tabulate(filtered_df, headers="keys", tablefmt="github"))    # MENAMPILKAN TABEL TANGGAL YANG SESUAI
            # MEMILIH INDEX YANG HENDAK DIHAPUS
            masukkan_hapus_presensi = input("\nMasukkan index yang hendak dihapus : ")
            print()

            if int(masukkan_hapus_presensi) in filtered_df.index.values.tolist():  # BILA INDEX YANG DIMASUKKAN ADA DI DALAH INDEKS SORTIRAN
                pilihan_absensi_hapus = input("Anda yakin?\nTekan [1] untuk menghapus\nTekan [2] atau [tombol lain] untuk membatalkan : ") # KONFIRMASI HENDAK MENGHAPUS ATAU TIDAK
                # DATA JADI DIHAPUS
                if pilihan_absensi_hapus == '1':
                    df = df.drop(int(masukkan_hapus_presensi))  # MENGHAPUS DATA
                    df = df.astype(str) # Konversi semua kolom ke dalam string sebelum menyimpan
                    # Simpan DataFrame yang telah diubah ke dalam file CSV
                    np.savetxt("presensi_database.csv",df,delimiter=',',fmt='% s')  
                    input(f"\nData {masukkan_hapus_presensi} berhasil dihapus!\n")  # IN-PROGRAM-NOTIFICATION DATA YANG TELAH DIHAPUS
                    print(f"Data saat ini :\n\n{tabulate.tabulate(df, headers="keys", tablefmt="github", showindex=False)}")    # DATA TERSISA
                # DATA TIDAK JADI DIHAPUS
                else:
                    input("\nMembatalkan ... Tekan [enter] untuk kembali ke menu utama")
                    main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN

            else:   # INDEX YANG DIPILIH BUKAN YANG DISORTIR
                print("Kesalahan input, index yang dimasukkan tidak dalam jangkauan sortir, atau data tidak ada")

            input("\nTekan [enter] untuk kembali ke Main Menu")
            main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN
        
        # FITUR 5.3

        else:
            main_page_admin()

    # FITUR 5

    elif menu_choice == '6':        # FITUR 6 KARYAWAN TERBAIK ATAU TERBURUK
        os.system('cls')
        print(f"++{'='*86}++\n|| {f'admin>menu utama>lihat data>lihat presensi karyawan>urutkan karyawan>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*21}L I H A T   P R E S E N S I   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('\r%A, %d %B %Y | %H:%M:%S')}\n")

        # opsi pemilihan waktu
        ulangAdmin4 = True
        while ulangAdmin4:
            rekap_choice = input("\nPilih jenis rekapitulasi\n[1] Minggu Ini\n[2] Bulan Ini\n[3] Tahun Ini\n[4] Minggu Lalu\n[5] Bulan Lalu\n[6] Kembali ke menu utama\n\nMasukkan pilihan : ")

            now = datetime.datetime.now()

            if rekap_choice in ['1', '2', '3']:  # minggu ini, bulan ini, tahun ini
                if rekap_choice == '1':  # minggu ini
                    rekap_choice_word = "minggu ini"
                    start_date = (now - datetime.timedelta(days=now.weekday())).strftime('%Y-%m-%d')
                    end_date = (now + datetime.timedelta(days=(6 - now.weekday()))).strftime('%Y-%m-%d')
                elif rekap_choice == '2':  # bulan ini
                    rekap_choice_word = "bulan ini"
                    start_date = f'{now.year}-{now.month:02d}-01'
                    last_day = calendar.monthrange(now.year, now.month)[1]
                    end_date = f'{now.year}-{now.month:02d}-{last_day}'
                else:  # tahun ini
                    rekap_choice_word = "tahun ini"
                    start_date = f'{now.year}-01-01'
                    end_date = f'{now.year}-12-31'
                ulangAdmin4 = False
            elif rekap_choice == '4':  # minggu lalu
                rekap_choice_word = "minggu lalu"
                start_date = (now - datetime.timedelta(days=now.weekday() + 7)).strftime('%Y-%m-%d')
                end_date = (now - datetime.timedelta(days=now.weekday() + 1)).strftime('%Y-%m-%d')
                ulangAdmin4 = False
            elif rekap_choice == '5':  # bulan lalu
                rekap_choice_word = "bulan lalu"
                last_month = now.month - 1 if now.month > 1 else 12
                last_month_year = now.year if now.month > 1 else now.year - 1
                last_month_last_day = calendar.monthrange(last_month_year, last_month)[1]
                start_date = f'{last_month_year}-{last_month:02d}-01'
                end_date = f'{last_month_year}-{last_month:02d}-{last_month_last_day}'
                ulangAdmin4 = False
            elif rekap_choice == '6':  # Back to main menu
                input("\nTekan [enter] untuk kembali ke menu utama")
                main_page_admin()
            else:
                input('Pilihan yang anda berikan tidak ada!\nCoba lagi')  # Invalid input, try again
                ulangAdmin4 = True

        # Convert data_presensi to DataFrame
        df = pd.DataFrame(data_presensi, columns=kolom_presensi)

        # Filter DataFrame based on selected date range
        filtered_df = df.loc[(df['Tanggal'] >= start_date) & (df['Tanggal'] <= end_date)]

        # Calculate attendance statistics for each employee
        def hitung_kehadiran(kehadiran_series):
            kehadiran_upper = kehadiran_series.str.upper()
            jumlah_hadir = (kehadiran_upper == 'HADIR').sum()
            jumlah_terlambat = (kehadiran_upper == 'TERLAMBAT').sum()
            return jumlah_hadir + jumlah_terlambat
        attendance_summary = filtered_df.groupby(['ID', 'Nama'])['Kehadiran'].apply(hitung_kehadiran).reset_index()
        attendance_summary.columns = ['ID', 'Nama', 'Total Kehadiran']

        # Ask for sorting order
        sort_order = input("\nPilih urutan\n[1] Dari terbaik ke terburuk\n[2] Dari terburuk ke terbaik\nMasukkan pilihan : ")

        # divide an conquer
        if sort_order == '1':
            sorted_df = attendance_summary.sort_values(by='Total Kehadiran', ascending=False)
        elif sort_order == '2':
            sorted_df = attendance_summary.sort_values(by='Total Kehadiran', ascending=True)
        else:
            print("\nPilihan yang anda berikan tidak ada!")
            input("\nTekan [enter] untuk kembali ke menu utama")
            main_page_admin()

        # Display sorted employees
        os.system('cls')
        print(f"++{'='*86}++\n|| {f'admin>menu utama>lihat data>lihat presensi karyawan>urutkan karyawan>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*21}L I H A T   P R E S E N S I   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('\r%A, %d %B %Y | %H:%M:%S')}\n\n")
        print(f'\nKaryawan dengan total kehadiran dari {"terbaik ke terburuk" if sort_order == "1" else "terburuk ke terbaik"} untuk periode "{rekap_choice_word}"\n')
        print(tabulate.tabulate(sorted_df, headers='keys', tablefmt='github', showindex=False))

        input("\nTekan [enter] untuk kembali ke menu utama")
        main_page_admin()

    elif menu_choice == '7':    # kembali ke launch page
        launchPage()

    # FITUR 6 SELESAI - UI : COMMENT : DESAIN

    elif menu_choice.upper() == 'N':
        # MENGIMPOR DATA HISTORI & MEMUNCULKAN NOTIFIKASI
        print("Notifikasi hari ini : ")
        for row in histori_column: 
            if datetime.datetime.now().strftime("%Y-%m-%d") in row:
                print(row)
        input("Tekan [enter] untuk kembali")
        main_page_admin()

    else:
        main_page_admin()    # salah input, kembali ke menu utama admin
    os.system('cls')

# FITUR ADMIN
      
# ------------------------------------------------------------------------------------------------------------------------------------------------------------


# HALAMAN UTAMA PEKERJA --------------------------------------------------------------------------------------------------------------------------------------

def main_page_employee():   # FITUR KARYAWAN
    os.system('cls')
    print(f'++{'='*86}++\n|| karyawan>menu utama>{' '*65}||\n++{'-'*86}++\n||{' '*86}||\n||{' '*24}M E N U   U T A M A   K A R Y A W A N{' '*25}||\n||{' '*86}||\n++{'='*86}++\nwaktu : {datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n')    # mengucapkan selamat datang
    
    # MENGIMPOR DATA KARYAWAN
    data_employee = []      # VARIABEL KOSONG UNTUK MENYIMPAN DATA KARYAWAN
    with open('employee_account_database.csv') as csvfile_employee: # MEMBUKA .CSV KARYAWAN
        reader_employee = csv.reader(csvfile_employee)
        for row in reader_employee:     # menjadikan file .csv menjadi list karyawan (menambahkan tiap baris pada .csv kedalam variabel data karyawan)
            data_employee.append(row)

    employee_column = [x[0] for x in data_employee]     # memecah data besar menjadi list-list data karyawan (menjadikan tiap data di list karyawan menjadi list-list terpisah)

    # MENGIMPOR DATA PRESENSI
    data_presensi = []  # VARIABEL KOSONG UNTUK MENYIMPAN DATA PRESENSI
    with open('presensi_database.csv') as csvfile_presensi:     # MEMBUKA .CSV PRESENSI
        reader_presensi = csv.reader(csvfile_presensi)      # menjadikan file .csv menjadi list presensi (menambahkan tiap baris pada .csv kedalam variabel data presensi)
        for row in reader_presensi:
            data_presensi.append(row)

    # MEMBUAT DATA PENGKONDISIAN UNTUK PENGECEKAN DATA SUDAH ADA ATAU BELUM
    data_presensi_cond = [] # VARIABEL KOSONG UNTUK MENYIMPAN DATA KONDISI
    g=0 # TRIGGER BARIS KE-
    with open('presensi_database.csv') as csvfile_presensi:     # MEMBUKA .CSV PRESENSI
        reader_presensi = csv.reader(csvfile_presensi)      #menjadikan file .csv menjadi list presensi (menambahkan tiap baris pada .csv kedalam variabel data presensi)
        for row in reader_presensi:
            data_presensi_cond.append(row)
            data_presensi_cond[g][-1] = ""      # MENAMBAHKAN TIAP DATA PRESENSI KE VARIABEL KONDISI DENGAN MENGHAPUS DATA KOLOM "WAKTU"
            g+=1

    # MENDETEKSI NAMA ADMIN MENGGUNAKAN ID
    if launch_ID in employee_column:    # ID DAN PASSCODE ADA DI DATABASE
        for x in range(0,len(data_employee)):       # mencocokkan ID hasil login dengan ID di database
            if launch_ID == data_employee[x][0]:    # ID DAN PASSCODE SESUAI DENGAN DATABASE ADMIN
                global tujuan   # index orang yang dituju saat menggunakan semua menu karyawan
                tujuan = x
                print(f'Selamat Datang, karyawan "{data_employee[x][1]}"! Apa yang ingin anda lakukan saat ini?\n') # selamat datang karyawan
    print('\nMenu:\n[1] PRESENSI SEKARANG!\n[2] Lihat Jadwal Shift\n[3] Lihat Rekapitulasi Presensi\n[4] Lihat Data Presensi Anda\n[5] Ajukan Lembur\n[6] Informasi Mengenai Program\n[7] Keluar') # pilihan menu karyawan
    menu_choice = input("Pilih menu : ")
    print()

    if menu_choice == '1':    # FITUR 1 PRESENSI SEKARANG
        os.system('cls')
        tanggal_presensi = datetime.datetime.now().strftime("%Y-%m-%d") # indikator tanggal riil

        # LOOPING UNTUK FITUR PRESENSI
        repeat_menu_choice_1 = True
        while repeat_menu_choice_1 :
            os.system('cls')
            menu_choice_1 = input(f'++{'='*86}++\n|| karyawan>menu utama>presensi sekarang!>{' '*46}||\n++{'-'*86}++\n||{' '*86}||\n||{' '*26}P R E S E N S I   S E K A R A N G !{' '*25}||\n||{' '*86}||\n++{'='*86}++\nwaktu : {datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n\nPilih Shift:\n[1] Pagi\n[2] Siang\n[3] Malam\n[4] Kembali Ke Menu\nPilih menu : ')  # UI PRESENSI SEKARANG DAN PILIHAN SHIFT

            if menu_choice_1 == '1':            # FITUR 1.1 PRESENSI SEKARANG>SHIFT PAGI
                if data_employee[tujuan][3] == 'True':  # KARYAWAN YANG HENDAK PRESENSI BENAR MERUPAKAN KARYAWAN SHIFT PAGI
                    repeat_menu_choice_1 = False
                    time_range = DateTimeRange(openPresensiPagi, closePresensiPagi)  # RANGE SHIFT PAGI
                    x = datetime.datetime.now().strftime("%H:%M:%S")    # DEKLARASI WAKTU TERBARU
                    
                    # BILA DALAM WAKTU GLOBAL PRESENSI
                    if x in DateTimeRange(openPresensiPagi,globalClosePresensi):   # ABSENSI GLOBAL DIBUKA
                        if x in time_range :    # DALAM RENTANG PRESENSI
                            status_kehadiran = "HADIR" 
                        elif x in timeRangePagi:    # TIDAK DALAM RENTANG PRESENSI TAPI MASIH PADA SHIFT
                            status_kehadiran = "TERLAMBAT"
                        else :          # PRESENSI DILUAR JAM SHIFT
                            input("\nPERHATIAN : Bukan jadwal presensi! Tekan [enter] untuk kembali ke menu utama")
                            status_kehadiran = "TIDAK HADIR"
                            main_page_employee()    # MENGEMBALIKAN KE MENU UTAMA
                        
                        # MEMBUAT DATA UNTUK DIMASUKKAN
                        data_baru = [tanggal_presensi, data_employee[tujuan][0],data_employee[tujuan][1],'PAGI',status_kehadiran,now_time.strftime("%H:%M:%S")]
                        # MEMBUAT DATA PENGKONDISIAN UNTUK MENGECEK DATA SUDAH ADA ATAU BELUM
                        data_baru_cond = [f'{tanggal_presensi}', f'{data_employee[tujuan][0]}', f'{data_employee[tujuan][1]}', 'PAGI', f'{status_kehadiran}', '']
                        
                        # MENDETEKSI APAKAH KARYAWAN SUDAH MELAKUKAN PRESENSI DI SHIFT YANG SAMA HARI INI
                        if data_baru_cond not in data_presensi_cond:    # KARYAWAN BELUM PRESENSI
                            # Menambahkan data baru ke dalam list data_presensi
                            data_presensi.append(data_baru)
                            # Membuka file CSV dalam mode penulisan dan menulis data baru ke dalamnya
                            with open('presensi_database.csv', 'w', newline='') as csvfile_presensi:
                                writer_presensi = csv.writer(csvfile_presensi)
                                writer_presensi.writerows(data_presensi)
                            input(f'\nPresensi : {tanggal_presensi},{now_time.strftime("%H:%M:%S")},{data_employee[tujuan][0]},{data_employee[tujuan][1]},PAGI,{status_kehadiran} \nPERHATIAN : Presensi berhasil direkam!\n\nTekan [enter] untuk kembali ke menu utama')   # IN-PROGRAM-NOTIFICATION DATA DICATAT
                        else:   # KARYAWAN SUDAH PRESENSI SEBELUMNYA
                            input(f'\nPERHATIAN : Data presensi "{tanggal_presensi},{data_employee[tujuan][0]},{data_employee[tujuan][1]},PAGI,{status_kehadiran}" sudah ada!\n\nTekan [enter] untuk kembali ke menu utama')    # IN-PROGRAM-NOTIFICATION DATA SUDAH ADA
                    
                    elif x in prePresensiPagi:     # ABSENSI GLOBAL BELUM DIBUKA
                        input("\nPERHATIAN : Waktu belum menunjukkan jadwal presensi!\n\nTekan [enter] untuk kembali ke menu utama")     # MENGEMBALIKAN KE MENU UTAMA

                else:   # KARYAWAN YANG HENDAK PRESENSI BUKAN MERUPAKAN KARYAWAN SHIFT PAGI
                    input("\nPERHATIAN : Bukan jadwal presensi shift anda! Tekan [enter] untuk melanjutkan")   # KEMBALI PILIH SHIFT PRESENSI
                    repeat_menu_choice_1 = True

            # FITUR 1.1

            elif menu_choice_1 == '2':          # FITUR 1.2 PRESENSI SEKARANG>SHIFT SIANG
                if data_employee[tujuan][4] == 'True':  # KARYAWAN YANG HENDAK PRESENSI BENAR MERUPAKAN KARYAWAN SHIFT SIANG
                    repeat_menu_choice_1 = False
                    time_range = DateTimeRange(openPresensiSiang, closePresensiSiang)   # RANGE SHIFT SIANG
                    x = datetime.datetime.now().strftime("%H:%M:%S")    # DEKLARASI WAKTU TERBARU

                    # BILA DALAM WAKTU GLOBAL PRESENSI
                    if x in DateTimeRange(openPresensiSiang, globalClosePresensi):  # ABSENSI GLOBAL DIBUKA
                        if x in time_range :    # DALAM RENTANG PRESENSI
                            status_kehadiran = "HADIR"
                        elif x in timeRangeSiang:   # TIDAK DALAM RENTANG PRESENSI TAPI MASIH PADA SHIFT
                            status_kehadiran = "TERLAMBAT"
                        else :          # PRESENSI DILUAR JAM SHIFT
                            input("\nPERHATIAN : Bukan jadwal presensi! Tekan [enter] untuk kembali ke menu utama")
                            status_kehadiran = "TIDAK HADIR"
                            main_page_employee()    # MENGEMBALIKAN KE MENU UTAMA
                        
                        # MEMBUAT DATA UNTUK DIMASUKKAN
                        data_baru = [tanggal_presensi, data_employee[tujuan][0],data_employee[tujuan][1],'SIANG',status_kehadiran,now_time.strftime("%H:%M:%S")]
                        # MEMBUAT DATA PENGKONDISIAN UNTUK MENGECEK DATA SUDAH ADA ATAU BELUM
                        data_baru_cond = [f'{tanggal_presensi}', f'{data_employee[tujuan][0]}', f'{data_employee[tujuan][1]}', 'SIANG', f'{status_kehadiran}', '']
                        
                        # MENDETEKSI APAKAH KARYAWAN SUDAH MELAKUKAN PRESENSI DI SHIFT YANG SAMA HARI INI
                        if data_baru_cond not in data_presensi_cond:    # KARYAWAN BELUM PRESENSI
                            # Menambahkan data baru ke dalam list data_presensi
                            data_presensi.append(data_baru)
                            # Membuka file CSV dalam mode penulisan dan menulis data baru ke dalamnya
                            with open('presensi_database.csv', 'w', newline='') as csvfile_presensi:
                                writer_presensi = csv.writer(csvfile_presensi)
                                writer_presensi.writerows(data_presensi)
                            input(f'\nPresensi : {tanggal_presensi},{now_time.strftime("%H:%M:%S")},{data_employee[tujuan][0]},{data_employee[tujuan][1]},SIANG,{status_kehadiran} \nPERHATIAN : Presensi berhasil direkam!\n\nTekan [enter] untuk kembali ke menu utama')  # IN-PROGRAM-NOTIFICATION DATA DICATAT
                        else:   # KARYAWAN SUDAH PRESENSI SEBELUMNYA
                            input(f'\nPERHATIAN : Data presensi "{tanggal_presensi},{data_employee[tujuan][0]},{data_employee[tujuan][1]},SIANG,{status_kehadiran}" sudah ada!\n\nTekan [enter] untuk kembali ke menu utama')   # IN-PROGRAM-NOTIFICATION DATA SUDAH ADA
                    
                    elif x in prePresensiSiang:  # ABSENSI GLOBAL BELUM DIBUKA
                        input("\nPERHATIAN : Waktu belum menunjukkan jadwal presensi!\n\nTekan [enter] untuk kembali ke menu utama")     # MENGEMBALIKAN KE MENU UTAMA
                
                else:   # KARYAWAN YANG HENDAK PRESENSI BUKAN MERUPAKAN KARYAWAN SHIFT SIANG
                    input("\nPERHATIAN : Bukan jadwal presensi shift anda! Tekan [enter] untuk melanjutkan")   # KEMBALI PILIH SHIFT PRESENSI
                    repeat_menu_choice_1 = True

            # FITUR 1.2

            elif menu_choice_1 == '3':          # FITUR 1.3 PRESENSI SEKARANG>SHIFT MALAM
                if data_employee[tujuan][5] == 'True':  # KARYAWAN YANG HENDAK PRESENSI BENAR MERUPAKAN KARYAWAN SHIFT MALAM
                    repeat_menu_choice_1 = False
                    time_range = DateTimeRange(openPresensiMalam, closePresensiMalam)  # RANGE SHIFT MALAM
                    x = datetime.datetime.now().strftime("%H:%M:%S")    # DEKLARASI WAKTU TERBARU

                    # BILA DALAM WAKTU GLOBAL PRESENSI
                    if x in DateTimeRange(openPresensiMalam,globalClosePresensi):   # ABSENSI GLOBAL DIBUKA
                        if x in time_range :    # DALAM RENTANG PRESENSI
                            status_kehadiran = "HADIR"
                        elif x in timeRangeMalam:   # TIDAK DALAM RENTANG PRESENSI TAPI MASIH PADA SHIFT
                            status_kehadiran = "TERLAMBAT"
                        else :          # PRESENSI DILUAR JAM SHIFT
                            input("\nPERHATIAN : Bukan jadwal presensi! Tekan [enter] untuk kembali ke menu utama")
                            status_kehadiran = "TIDAK HADIR"
                            main_page_employee()    # MENGEMBALIKAN KE MENU UTAMA
                        
                        # MEMBUAT DATA UNTUK DIMASUKKAN
                        data_baru = [tanggal_presensi, data_employee[tujuan][0],data_employee[tujuan][1],'MALAM',status_kehadiran,now_time.strftime("%H:%M:%S")]
                        # MEMBUAT DATA PENGKONDISIAN UNTUK MENGECEK DATA SUDAH ADA ATAU BELUM
                        data_baru_cond = [f'{tanggal_presensi}', f'{data_employee[tujuan][0]}', f'{data_employee[tujuan][1]}', 'MALAM', f'{status_kehadiran}', '']
                        
                        # MENDETEKSI APAKAH KARYAWAN SUDAH MELAKUKAN PRESENSI DI SHIFT YANG SAMA HARI INI
                        if data_baru_cond not in data_presensi_cond:    # KARYAWAN BELUM PRESENSI
                            # Menambahkan data baru ke dalam list data_presensi
                            data_presensi.append(data_baru)
                            # Membuka file CSV dalam mode penulisan dan menulis data baru ke dalamnya
                            with open('presensi_database.csv', 'w', newline='') as csvfile_presensi:
                                writer_presensi = csv.writer(csvfile_presensi)
                                writer_presensi.writerows(data_presensi)
                            input(f'\nPresensi : {tanggal_presensi},{now_time.strftime("%H:%M:%S")},{data_employee[tujuan][0]},{data_employee[tujuan][1]},MALAM,{status_kehadiran} \nPERHATIAN : Presensi berhasil direkam!\n\nTekan [enter] untuk kembali ke menu utama')  # IN-PROGRAM-NOTIFICATION DATA DICATAT
                        else:  # KARYAWAN SUDAH PRESENSI SEBELUMNYA
                            input(f'\nPERHATIAN : Data presensi "{tanggal_presensi},{data_employee[tujuan][0]},{data_employee[tujuan][1]},MALAM,{status_kehadiran}" sudah ada!\n\nTekan [enter] untuk kembali ke menu utama')   # IN-PROGRAM-NOTIFICATION DATA SUDAH ADA
                    
                    elif x in prePresensiMalam:  # ABSENSI GLOBAL BELUM DIBUKA
                        input("\nPERHATIAN : Waku belum menunjukkan jadwal presensi!\n\nTekan [enter] untuk kembali ke menu utama")
                
                else:   # KARYAWAN YANG HENDAK PRESENSI BUKAN MERUPAKAN KARYAWAN SHIFT MALAM
                    input("\nPERHATIAN : Bukan jadwal presensi anda! Tekan [enter] untuk melanjutkan")   # KEMBALI PILIH SHIFT PRESENSI
                    repeat_menu_choice_1 = True
            
            # FITUR 1.3 

            elif menu_choice_1 == '4':          # FITUR 1.4 PRESENSI SEKARANG>KEMBALI KE MENU UTAMA
                repeat_menu_choice_1 = False
            
            # FITUR 1.4

            else:                               # SALAH INPUT, COBA LAGI
                repeat_menu_choice_1 = True

        main_page_employee()

    # FITUR 1

    elif menu_choice == '2':  # FITUR 2 LIHAT JADWAL SHIFT ANDA
        os.system('cls')  # Membersihkan layar konsol
        print(f"++{'='*86}++\n|| karyawan>menu utama>lihat jadwal shift>{' '*46}||\n++{'-'*86}++\n||{' '*86}||\n||{' '*21}L I H A T   J A D W A L   S H I F T   A N D A{' '*20}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('%A, %d %B %Y | %H:%M:%S')}\n")    # UI LIHAT JADWAL SHIFT
        print("Shift anda minggu ini:\n")

        # MEMASUKKAN DATA KE PANDAS
        df = pd.DataFrame(data_employee, columns=kolom_employee)
        # Filter DataFrame berdasarkan ID yang sudah login
        filtered_df = df.loc[df['ID'] == launch_ID]

        # Daftar shift
        shifts = [
            ("Shift 1", '"PAGI"\n04:00:00 - 10:00:00'),
            ("Shift 2", '"SIANG"\n10:00:00 - 16:00:00'),
            ("Shift 3", '"MALAM"\n16:00:00 - 22:00:00')
        ]

        left, right = 0, len(shifts) - 1
        statShift = True  # Asumsi awal tidak ada shift

        while left <= right:
            mid = (left + right) // 2
            shift_key, shift_text = shifts[mid]
            if filtered_df.loc[tujuan, shift_key] == 'True':
                print(shift_text)
                statShift = False
                left = mid + 1  # Lanjutkan pencarian untuk shift berikutnya
            else:
                right = mid - 1  # Shift tidak ditemukan, kurangi jangkauan pencarian

        if statShift:
            print('"TIDAK ADA"')

        input("\n\nTekan [enter] untuk kembali ke Main Menu")
        main_page_employee()  # MENGEMBALIKAN KE MENU UTAMA
    
    # FITUR 2

    elif menu_choice == '3':  # FITUR 3 REKAPITULASI PRESENSI
        ulangEmployee3 = True   # LOOPING UNTUK MENU REKAPITULASI PRESENSI
        while ulangEmployee3:

            os.system('cls')
            print(f"++{'='*86}++\n|| karyawan>menu utama>rekapitulasi presensi>{' '*43}||\n++{'-'*86}++\n||{' '*86}||\n||{' '*23}R E K A P I T U L A S I   P R E S E N S I{' '*22}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}") # UI REKAPITULASI PRESENSI
            with open('presensi_database.csv', 'r') as presensi_file:   # MENGIMPOR DATA PRESENSI
                data_presensi = presensi_file.readlines()

            # Membuat DataFrame Pandas dari data presensi
            df = pd.DataFrame([entry.strip().split(',') for entry in data_presensi], columns=kolom_presensi)
            # Filter DataFrame berdasarkan ID yang sudah login
            filtered_df = df.loc[df['ID'] == launch_ID]

            # Pilihan untuk rekap mingguan atau bulanan
            rekap_choice = input("\nPilih jenis rekapitulasi\n[1] Minggu Ini\n[2] Minggu Lalu\n[3] Bulan Ini\n[4] Bulan Lalu\n[5] Kembali ke menu utama\n\nMasukkan pilihan : ")

            now = datetime.datetime.now()

            if rekap_choice == '1':  # Minggu Ini
                rekap_choice_word = "minggu ini"
                ulangEmployee3 = False
                start_date = (now - timedelta(days=now.weekday())).strftime('%Y-%m-%d')
                end_date = (now + timedelta(days=(6 - now.weekday()))).strftime('%Y-%m-%d')
                total_days = 7

            elif rekap_choice == '2':  # Minggu Lalu
                rekap_choice_word = "minggu lalu"
                ulangEmployee3 = False
                start_date = (now - timedelta(days=(now.weekday() + 7))).strftime('%Y-%m-%d')
                end_date = (now - timedelta(days=now.weekday() + 1)).strftime('%Y-%m-%d')
                total_days = 7

            elif rekap_choice == '3':  # Bulan Ini
                rekap_choice_word = "bulan ini"
                ulangEmployee3 = False
                start_date = f'{now.year}-{now.month:02d}-01'
                last_day = calendar.monthrange(now.year, now.month)[1]
                end_date = f'{now.year}-{now.month:02d}-{last_day}'
                total_days = last_day

            elif rekap_choice == '4':  # Bulan Lalu
                rekap_choice_word = "bulan lalu"
                ulangEmployee3 = False
                last_month = (now.replace(day=1) - timedelta(days=1)).replace(day=1)
                start_date = f'{last_month.year}-{last_month.month:02d}-01'
                last_day = calendar.monthrange(last_month.year, last_month.month)[1]
                end_date = f'{last_month.year}-{last_month.month:02d}-{last_day}'
                total_days = last_day

            elif rekap_choice == '5':
                input("\nTekan [enter] untuk kembali ke menu utama")
                main_page_employee()    # MENGEMBALIKAN KE MENU UTAMA

            else:
                input('Pilihan yang anda berikan tidak ada!\nCoba lagi')    # KESALAHAN INPUT, KEMBALI KE NEMU REKAP
                ulangEmployee3 = True
        
        # Filter DataFrame berdasarkan tanggal
        filtered_df = filtered_df.loc[(filtered_df['Tanggal'] >= start_date) & (filtered_df['Tanggal'] <= end_date)]

        # Menghitung statistik kehadiran
        total_kehadiran_tepat_waktu = len(filtered_df[filtered_df['Kehadiran'].str.upper() == 'HADIR'])
        total_terlambat = len(filtered_df[filtered_df['Kehadiran'].str.upper() == 'TERLAMBAT'])
        total_kehadiran = total_kehadiran_tepat_waktu + total_terlambat
        total_tidak_hadir = len(filtered_df[filtered_df['Kehadiran'].str.upper() == 'TIDAK HADIR'])

        total_hari_kerja = total_kehadiran + total_tidak_hadir  # Total hari kerja dihitung berdasarkan jumlah data presensi

        # Menampilkan statistik kehadiran
        os.system('cls')
        print(f'++{'='*86}++\n|| {'karyawan>menu utama>rekapitulasi presensi>'f"{rekap_choice_word}"'>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{' '*23}R E K A P I T U L A S I   P R E S E N S I{' '*22}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n\nMenampilkan rekapitulasi "{rekap_choice_word.upper()}"\n{start_date} | {end_date}\n\n\nTOTAL HADIR : {total_kehadiran}')  # UI HASIL REKAPAN

        # Rincian Total Kehadiran
        print("    Rincian:")
        print(f"      -Total Hadir Tepat Waktu: {total_kehadiran_tepat_waktu}")
        print(f"      -Total Terlambat: {total_terlambat}")

        print(f"\nTOTAL TIDAK HADIR : {total_tidak_hadir}")

        # Persentase Kehadiran
        if total_hari_kerja > 0:
            attendance_percentage = round((total_kehadiran / total_hari_kerja * 100))
            print(f"\nPERSENTASE KEHADIRAN ({start_date} sampai {end_date}): {attendance_percentage}% ({total_kehadiran} dari {total_hari_kerja} hari kerja)")
        else:
            print("\nTidak ada data kehadiran pada periode yang dipilih.")

        input("\n\n\nTekan [enter] untuk kembali ke Main Menu")
        main_page_employee()    # MENGEMBALIKAN KE MENU UTAMA

    # FITUR 3

    elif menu_choice == '4':  # FITUR 4 LIHAT DATA PRESENSI ANDA

        os.system('cls')  # Membersihkan layar konsol
        print(f'++{'='*86}++\n|| {'karyawan>menu utama>lihat data presensi anda':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*20}L I H A T   D A T A   P R E S E N S I   A N D A':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n')
        
        with open('presensi_database.csv', 'r') as presensi_file:   # MEMBUKA DATABASE PRESENSI
            data_presensi = presensi_file.readlines()
        # MENGUBAH DATA MENJADI TABEL PANDAS
        df = pd.DataFrame([entry.strip().split(',') for entry in data_presensi],columns=["Tanggal", "ID", "Nama", "Shift","kehadiran","Waktu"])
        
        filtered_df = df.loc[df['ID'] == launch_ID] # DEKLARASI SIAPA YANG HENDAK DIREKAP

        # MEMILIH JENIS REKAP
        rekap_choice = input("\nPilih jenis rekapitulasi\n[1] Minggu Ini\n[2] Minggu Lalu\n[3] Bulan Ini\n[4] Bulan Lalu\n[5] Lihat data keseluruhan\nSilahkan pilih menu : ")
        os.system('cls')
        now = datetime.datetime.now()

        if rekap_choice == '1':  # Minggu Ini
            rekap_choice_word = 'minggu Ini'
            start_date = (now - timedelta(days=now.weekday())).strftime('%Y-%m-%d')
            end_date = (now + timedelta(days=(6 - now.weekday()))).strftime('%Y-%m-%d')

        elif rekap_choice == '2':  # Minggu Lalu
            rekap_choice_word = 'minggu Lalu'
            start_date = (now - timedelta(days=(now.weekday() + 7))).strftime('%Y-%m-%d')
            end_date = (now - timedelta(days=now.weekday() + 1)).strftime('%Y-%m-%d')

        elif rekap_choice == '3':  # Bulan Ini
            rekap_choice_word = 'bulan Ini'
            start_date = f'{now.year}-{now.month:02d}-01'
            last_day = calendar.monthrange(now.year, now.month)[1]
            end_date = f'{now.year}-{now.month:02d}-{last_day}'

        elif rekap_choice == '4':  # Bulan Lalu
            rekap_choice_word = 'bulan Lalu'
            last_month = (now.replace(day=1) - timedelta(days=1)).replace(day=1)
            start_date = f'{last_month.year}-{last_month.month:02d}-01'
            last_day = calendar.monthrange(last_month.year, last_month.month)[1]
            end_date = f'{last_month.year}-{last_month.month:02d}-{last_day}'
            
        elif rekap_choice == '5' :  # semua
            rekap_choice_word = 'semua'
            start_date = '...'
            end_date = '...'

        else :  # KESALAHAN INPUT
            print("Input yang anda masukan salah")
            input("Tekan enter untuk kembali ke menu")
            main_page_employee()    # MENGEMBALIKAN KE MENU UTAMA
        
        # MENAMPILKAN DATA REKAP
        print(f'++{'='*86}++\n|| {f'karyawan>menu utama>lihat data presensi anda>{rekap_choice_word}':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*20}L I H A T   D A T A   P R E S E N S I   A N D A':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n\n\nMenampilkan data presensi "{rekap_choice_word.upper()}"\n{start_date} | {end_date}\n')   # UI HASIL REKAP
        if rekap_choice in '1234':  # BILA MEMILIH SALAH SATU PILIHAN DARI 1234
            filtered_df = filtered_df.loc[(filtered_df['Tanggal'] >= start_date) & (filtered_df['Tanggal'] <= end_date)]
            print(tabulate.tabulate(filtered_df, headers="keys", tablefmt="github", showindex=False))
        elif rekap_choice == '5':   # BILA MEMILIH 5 : SEMUA
            print (tabulate.tabulate(filtered_df, headers="keys", tablefmt="github", showindex=False))

        input("\nTekan [enter] untuk kembali ke Main Menu")
        main_page_employee()    # MENGEMBALIKAN KE MENU UTAMA
    
    # FITUR 4

    elif menu_choice == '5':  # FITUR 5 Pangajuan Lembur
        os.system('cls')
        def baca_data_karyawan():
            data_karyawan = []
            try:
                with open("employee_account_database.csv", "r", newline="") as csvfile:
                    reader = csv.DictReader(csvfile, fieldnames=["ID", "Nama", "Posisi", "ShiftPagi", "ShiftSiang", "ShiftMalam", "Password"])
                    for row in reader:
                        data_karyawan.append({
                            "ID": row["ID"],
                            "Nama": row["Nama"],
                            "Posisi": row["Posisi"],
                            "Shift": {
                                "Pagi": row["ShiftPagi"] == "True",
                                "Siang": row["ShiftSiang"] == "True",
                                "Malam": row["ShiftMalam"] == "True"
                            },
                            "Password": row["Password"]
                        })
            except KeyError as e:
                print(f"Error: Kolom {e} tidak ditemukan di file CSV.")
            return data_karyawan

        def hitung_jam_lembur(jam_pulang_lembur, jam_pulang):
            jam_pulang_lembur_h, jam_pulang_lembur_m = map(int, jam_pulang_lembur.split(':'))
            jam_pulang_h, jam_pulang_m = map(int, jam_pulang.split(':'))

            total_menit_pulang_lembur = jam_pulang_lembur_h * 60 + jam_pulang_lembur_m
            total_menit_pulang = jam_pulang_h * 60 + jam_pulang_m

            if total_menit_pulang_lembur > total_menit_pulang:
                total_menit_lembur = total_menit_pulang_lembur - total_menit_pulang
                return total_menit_lembur // 60
            else:
                return 0

        def baca_data_lembur():
            data_lembur = []
            try:
                with open("data_lembur.csv", "r", newline="") as csvfile:
                    reader = csv.DictReader(csvfile, fieldnames=["ID", "Jam Lembur"])
                    next(reader) 
                    for row in reader:
                        data_lembur.append({
                            "ID": row["ID"],
                            "Jam Lembur": int(row["Jam Lembur"]) 
                        })
            except FileNotFoundError:
                print("File data_lembur.csv tidak ditemukan, memulai dengan data lembur kosong.")
            return data_lembur

        def catat_lembur(jam_pulang_lembur):
            global data_lembur
            data_karyawan = baca_data_karyawan()
            for data in data_karyawan:
                if data["ID"] == launch_ID:
                    if data["Shift"]["Pagi"]:
                        jam_selesai_shift = "09:59"
                    elif data["Shift"]["Siang"]:
                        jam_selesai_shift = "15:59"
                    elif data["Shift"]["Malam"]:
                        jam_selesai_shift = "21:59"
                    else:
                        print("Error: Tidak ada shift yang dipilih.")
                        return

                    jam_lembur = 0
                    if jam_pulang_lembur > jam_selesai_shift:
                        jam_lembur = hitung_jam_lembur(jam_pulang_lembur, jam_selesai_shift)

                    data_lembur.append({"ID": launch_ID, "Jam Lembur": jam_lembur})
                    print(f"Lembur untuk ID '{launch_ID}' berhasil dicatat.")
                    return
            print(f"Error: Employee dengan ID '{launch_ID}' tidak ditemukan.")

        def buat_csv_lembur():
            with open("data_lembur.csv", "w", newline="") as csvfile:
                fieldnames = ["ID", "Jam Lembur"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for data in data_lembur:
                    writer.writerow(data)
            print("Data lembur telah disimpan ke file data_lembur.csv")

        def lihat_data_lembur():
            global data_lembur
            ditemukan = False
            for data in data_lembur:
                if data["ID"] == launch_ID:
                    print(f"ID: {data['ID']}, Jam Lembur: {data['Jam Lembur']} jam")
                    ditemukan = True
            if not ditemukan:
                print(f"Data lembur untuk ID '{launch_ID}' tidak ditemukan.")

        def hapus_lembur():
            global data_lembur
            if not data_lembur:
                print("Tidak ada data lembur untuk dihapus.")
                return

            print("Data Lembur:")
            for idx, data in enumerate(data_lembur):
                print(f"{idx + 1}. ID: {data['ID']}, Jam Lembur: {data['Jam Lembur']} jam")

            pilihan_hapus = int(input("Pilih nomor lembur yang ingin dihapus: ")) - 1
            if 0 <= pilihan_hapus < len(data_lembur):
                data_lembur.pop(pilihan_hapus)
                print("Data lembur berhasil dihapus.")
            else:
                print("Pilihan tidak valid.")

        def menu():
            global data_lembur
            data_lembur = baca_data_lembur()
            while True:
                print("\nMenu:")
                print("1. Ajukan Lembur")
                print("2. Lihat Data Lembur Diri Sendiri")
                print("3. Hapus Lembur")
                print("4. Keluar")
                
                pilihan = input("Pilih opsi: ")
                
                if pilihan == "1":
                    jam_pulang_lembur = input("Masukkan jam pulang lembur (HH:MM): ")
                    catat_lembur(jam_pulang_lembur)
                    
                elif pilihan == "2":
                    lihat_data_lembur()
            
                elif pilihan == "3":
                    hapus_lembur()
                
                elif pilihan == "4":
                    buat_csv_lembur()
                    main_page_employee()
                
                else:
                    print("Pilihan tidak valid, silakan coba lagi.")
        menu()

    elif menu_choice == '6':  # FITUR 6 EULA
        os.system('cls')
        print(eula_text)
        input("\nTekan [enter] untuk kembali ke menu utama")
        main_page_employee()    # MENGEMBALIKAN KE MENU UTAMA

    # FITUR 6 SELESAI - UI : COMMENT : DESAIN

    elif menu_choice == '7':  # FITUR 7 KELUAR
        launch_page_condition = True
        launchPage()    # KEMBALI KE LAUNCH PAGE

    # FITUR 7 SELESAI - UI : COMMENT : DESAIN

    else:       # BILA SALAH INPUT
        main_page_employee()

# FITUR KARYAWAN 

# ------------------------------------------------------------------------------------------------------------------------------------------------------------


# FITUR AKUN PERTAMA v --------------------------------------------------------------------------------------------------------------------------

def akun_pertama():
    os.system('cls')

    # apabila database akun karyawan belum ada
    if not(Path('employee_account_database.csv').is_file()):
        #buat file dahulu sebelum mengakses fungsi tambah supaya bisa menambahkan header dulu
        employee = open('employee_account_database.csv', 'w')
        employee.close()

    # apabila database presensi belum ada
    if not(Path('presensi_database.csv').is_file()):
        #buat file dahulu sebelum mengakses fungsi tambah supaya bisa menambahkan header dulu
        presensi = open('presensi_database.csv', 'w')
        presensi.close()

    # apabila database admin belum ada
    if not(Path('admin_account_database.csv').is_file()):
        #buat file dahulu sebelum mengakses fungsi tambah supaya bisa menambahkan header dulu

        # data admin pertama
        first_account_ID     = str(input("Anda adalah admin pertama! \nMasukkan ID anda           : "))
        first_account_nama   = str(input("Masukkan Nama Lengkap anda : "))
        first_account_posisi = str(input("Masukkan Jabatan anda      : "))
        first_Account_pass   = str(input("Masukkan passkey anda      : "))

        # memasukkan admin pertama 
        first_input = f"{first_account_ID.upper()},{first_account_nama.upper()},{first_account_posisi.upper()},TRUE,TRUE,TRUE,TRUE,TRUE,FALSE,FALSE{first_Account_pass}"

        with open('admin_account_database.csv', 'w', newline='') as fileAdmincsv:
            admin_list = csv.DictWriter(fileAdmincsv, fieldnames=[first_input],  delimiter='/') 
            admin_list.writeheader()

    # apabila database histori belum ada
    if not(Path('histori_database.csv').is_file()):
        #buat file dahulu sebelum mengakses fungsi tambah supaya bisa menambahkan header dulu
        presensi = open('histori_database.csv', 'w')
        presensi.close()

# FITUR AKUN PERTAMA

# ------------------------------------------------------------------------------------------------------------------------------------------------------------



# BACKEND : OTOMATIS PRESENSI BILA TIDAK HADIR v ------------------------------------------------------------------------------------------------------------------

def backendAutoPresensi():
    # MEMBUAT PENGECEK DATA PRESENSI SUDAH ADA ATAU BELUM
    # INDIKATOR DATABASE KARYAWAN
    data_employee = []
    with open('employee_account_database.csv') as csvfile_employee:
        reader_employee = csv.reader(csvfile_employee)
        for row in reader_employee:
            data_employee.append(row)

    # DATABASE PRESENSI
    data_presensi = []
    with open('presensi_database.csv') as csvfile_presensi:
        reader_presensi = csv.reader(csvfile_presensi)
        for row in reader_presensi:
            data_presensi.append(row)

    # INDIKATOR DATABASE PRESENSI
    data_presensi_cond = []
    g=0
    with open('presensi_database.csv') as csvfile_presensi:
        reader_presensi = csv.reader(csvfile_presensi)
        for row in reader_presensi:
            data_presensi_cond.append(row)
            data_presensi_cond[g][-1] = ""
            data_presensi_cond[g][-2] = ""
            g+=1

    # MENDETEKSI ADA TIDAKNYA DATA DI HARI INI
    dataHistory = []
    with open('histori_database.csv') as csvfile_histori:
        reader_histori = csv.reader(csvfile_histori)
        for row in reader_histori:
            dataHistory.append(row)
    histori_column = [x[0] for x in dataHistory]
            
    # MENDETEKSI ADA TIDAKNYA DATA PRESENSI
    if waktuRealBackend not in histori_column:
        tanggalUpdateHistori = [waktuRealBackend]
        with open('histori_database.csv', 'a', newline='') as csvfile_histori:    # notifikasi ke admin
            writer_histori = csv.writer(csvfile_histori,quoting=csv.QUOTE_NONE, escapechar=None)
            writer_histori.writerow(tanggalUpdateHistori)

    for tujuan in range (0, len(data_employee)):

        hari_seminggu = ["SENIN", "SELASA", "RABU", "KAMIS", "JUMAT", "SABTU", "MINGGU"]
        for nomor_hari in range(3,9):
            if data_employee[tujuan][nomor_hari] == 'True':    
                data_baru = [tanggal_presensi, data_employee[tujuan][0],data_employee[tujuan][1],hari_seminggu[nomor_hari],'TIDAK HADIR',datetime.datetime.now().strftime("%H:%M:%S")]
                data_baru_cond = [f'{tanggal_presensi}', f'{data_employee[tujuan][0]}', f'{data_employee[tujuan][1]}', hari_seminggu[nomor_hari], '', '']
                dataUpdateHistori = [f'{tanggal_presensi} {hari_seminggu[nomor_hari]} Karyawan {data_employee[tujuan][0]} {data_employee[tujuan][1]} tidak presensi']

                if (data_baru_cond not in data_presensi_cond) and ((datetime.datetime.now().strftime("%H:%M:%S") )not in (pre_presensi and time_range_kerja)) and (dataUpdateHistori not in dataHistory):
                    data_presensi.append(data_baru)   # Menambahkan data baru ke dalam list data_presensi
                    with open('presensi_database.csv', 'w', newline='') as csvfile_presensi:    # Membuka file CSV dalam mode penulisan dan menulis data baru ke dalamnya
                        writer_presensi = csv.writer(csvfile_presensi)
                        writer_presensi.writerows(data_presensi)
                    with open('histori_database.csv', 'a', newline='') as csvfile_histori:    # notifikasi ke admin
                        writer_histori = csv.writer(csvfile_histori,quoting=csv.QUOTE_NONE, escapechar='_')
                        writer_histori.writerows([dataUpdateHistori])
                else:
                    pass


# BACKEND : OTOMATIS PRESENSI BILA TIDAK HADIR

# ------------------------------------------------------------------------------------------------------------------------------------------------------------


# PERKOLOMAN DAN DESAIN---------------------------------------------------------------------------------------------------------------------------------------

# kolom esensial
kolom_admin    = ['ID','Nama','Posisi','Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Password']
kolom_employee = ['ID','Nama','Posisi','Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Password']
kolom_presensi = ["Tanggal", "ID", "Nama", "Hari Kerja", "Kehadiran", "Waktu"]

# lama freeze welcome page
delayWelcome = 3

# menentukan berapa karyawan dalam toko
# qKasir = 3
# qStaf = 2*qKasir
# qKasirPagi = 1
# qKasirSiang = 1
# qKasirMalam = 1
# qStafPagi = 2*qKasirPagi
# qStafSiang = 2*qKasirSiang
# qStafMalam = 2*qKasirMalam

#logo-logo
logoPart1 = (r"  _    _       _____                      ")
logoPart2 = (r" | |  | |     / ____|                     ")
logoPart3 = (r" | |  | |_ __| (___   ___ _ __   ___ ___  ")
logoPart4 = (r" | |  | | '_ \____ \ / _ \ '_ \ / __/ _ \ ")
logoPart5 = (r" | |__| | |_) |___) |  __/ | | | (_|  __/ ")
logoPart6 = (r"  \____/| .__/_____/ \___|_| |_|\___\___| ")
logoPart7 = (r"        | |                               ")
logoPart8 = (r"        |_|                               ")

logo = f'{logoPart1}\n{logoPart2}\n{logoPart3}\n{logoPart4}\n{logoPart5}\n{logoPart6}\n{logoPart7}\n{logoPart8}'
logoLaunch = f'++{'='*50}++\n||{' '*50}||\n||{' '*4}{logoPart1}{' '*4}||\n||{' '*4}{logoPart2}{' '*4}||\n||{' '*4}{logoPart3}{' '*4}||\n||{' '*4}{logoPart4}{' '*4}||\n||{' '*4}{logoPart5}{' '*4}||\n||{' '*4}{logoPart6}{' '*4}||\n||{' '*4}{logoPart7}{' '*4}||\n||{' '*4}{logoPart8}{' '*4}||\n||{' '*50}||\n||{' '*4}UpSence : Aplikasi Presensi Berbasis Python{' '*3}||\n||{' '*50}||\n||{' '*13}by ©Kelompok 2 TA Algo2{' '*14}||\n++{'='*50}++'
logoBorder = f'++{'='*86}++\n||{' '*22}{logoPart1}{' '*22}||\n||{' '*22}{logoPart2}{' '*22}||\n||{' '*22}{logoPart3}{' '*22}||\n||{' '*22}{logoPart4}{' '*22}||\n||{' '*22}{logoPart5}{' '*22}||\n||{' '*22}{logoPart6}{' '*22}||\n||{' '*22}{logoPart7}{' '*22}||\n||{' '*22}{logoPart8}{' '*22}||\n||{' '*86}||\n||{' '*27}Aplikasi Presensi Berbasis Python{' '*26}||\n++{'='*86}++'

launchInterface = f"+{'='*88}+\n|{' '*88}|\n|{' '*20}SELAMAT DATANG DI LAUNCH PAGE APLIKASI PRESENSI{' '*21}|\n|{' '*88}|\n+{'='*88}+\n"
loginInterface = f"+{'='*88}+\n|{' '*30}SELAMAT DATANG DI MENU LOGIN{' '*30}|\n|{' '*25}silahkan masukkan kredensial LOGIN anda{' '*24}|\n+{'='*88}+"

# eula
eula_text = f"""\n{logoBorder}

                            END USER LICENSE AGREEMENT (EULA)

Selamat datang di Program UpSence, program sistem presensi karyawan toko berbasis terminal.
UpSence dibuat menggunakan bahasa pemrograman Python.

Sebelum menggunakan Program UpSence harap baca ketentuan penggunaan program kami berikut: 
        
    1. Program ini hanya boleh digunakan oleh karyawan yang telah terdaftar dalam sistem.
    2. Dilarang menggunakan program ini untuk tujuan selain yang telah ditentukan.
    3. Setiap aktivitas yang direkam oleh pengguna dalam program berkaitan dengan
       pengguna yang bersangkutan menjadi tanggung jawab yang bersangkutan.
    4. Kami akan menyimpan data yang terkait dengan penggunaan program ini sesuai dengan
       kebijakan.
    5. DILARANG mengubah dan memodifikasi program ini kemudian mendistribusikannya
       tanpa seizin kami
    6. Pengguna bisa menggunakan Program ini pada perangkat komputer dengan sistem operasi
       Windows dan MacOS
    7. Jika program ini akan digunakan pada sistem operasi Mac, maka perlu mengubah
       perintah 'cls' menjadi 'clear'
        
Dengan melanjutkan, Anda menyetujui semua syarat dan ketentuan diatas.


        Setelah anda menyetujui ketentuan diatas, berikut adalah fitur UpSence:

-Fitur Admin
    1. Admin dapat menambah dan mengurangi pengguna yang dapat menggunakan program ini.
    2. Admin dapat melihat dan mengedit Data Karyawan dan Presensi Karyawan,
       kemudian bisa melihat rekap atas presensi tersebut.
        
-Fitur Karyawan
    1. Karyawan dapat melakukan presensi sesuai dengan ketentuan yang dibuat oleh admin
    2. Apabila Karyawan melakukan presensi diluar jam presensi namun masih di jam shift
       maka akan tercatat sebagai terlambat, namun apabila sudah keluar dari jam shift,
       maka akan tercatat sebagai tidak hadir.
    3. Karyawan dapat melakukan pengecekan terhadap presensinya sendiri,
       seperti shift dan rekapitulasi presensi miliknya sendiri.

-Informasi tambahan
    1. Pada menu rekapitulasi presensi terdapat fitur rekapitulasi,
       yang terdiri dari mingguan, bulanan, dan seluruh data presensi yang bisa dilihat.
    2. Karyawan hanya dapat melihat rekapitulasi presensinya sendiri,
       sedangkan Admin dapat melihat seluruh Presensi Karyawan.
        

                    Terima kasih telah menggunakan program UpSence


©Kelompok 2 TA Algo1
"""

# ------------------------------------------------------------------------------------------------------------------------------------------------------------


# PERWAKTUAN DAN PERKALENDERAN--------------------------------------------------------------------------------------------------------------------------------

# waktu-waktu
now_time = datetime.datetime.now()
waktuReal = now_time.strftime("\r%A, %d %B %Y | %H:%M:%S")
waktuRealTanggal = now_time.strftime("%Y-%m-%d")
waktuRealJam = now_time.strftime("%H:%M:%S")
tanggal_presensi = datetime.datetime.now().strftime("%Y-%m-%d")

# # range jam shift
# timeRangePagi = DateTimeRange("04:00:00", "09:59:59")
# timeRangeSiang = DateTimeRange("10:00:00", "15:59:59")
# timeRangeMalam = DateTimeRange("16:00:00", "21:59:59")

# range jam kerja
time_range_kerja = DateTimeRange("08:00:00", "16:59:59")
pre_presensi = DateTimeRange("00:00:00", "07:59:59")
open_presensi = "08:00:00"
close_presensi = "17:00:00"
global_close_presensi = "23:59:59"

# # range presensi shift
# prePresensiPagi = DateTimeRange("00:00:00", "03:59:59")
# openPresensiPagi = "04:00:00"
# closePresensiPagi = "05:00:00"
# prePresensiSiang = DateTimeRange("00:00:00", "09:59:59")
# openPresensiSiang = "10:00:00"
# closePresensiSiang = "11:00:00"
# prePresensiMalam = DateTimeRange("00:00:00", "15:59:59")
# openPresensiMalam = "16:00:00"
# closePresensiMalam = "17:00:00"

# globalClosePresensi = "23:59:59"

# untuk absensi otomatis
waktuRealBackend = now_time.strftime("%A %d %B %Y")

# memperbolehkan operasi dengan 0
def calculate_percentage(present_days, total_days):
    if total_days != 0:
        return present_days / total_days * 100
    else:
        return 0.0 #biar gak 0

# ------------------------------------------------------------------------------------------------------------------------------------------------------------


# EKSEKUSI----------------------------------------------------------------------------------------------------------------------------------------------------

akun_pertama()
backendAutoPresensi()
launchPage()
