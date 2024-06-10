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
import matplotlib.pyplot as plt         # import matlib agar bisa menampilkan diagram
import tkinter as tk                    # import tkinter agar bisa engatur letak diagram agar tertata

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
                        if launch_ID == data_admin[x][0] and launchPass == data_admin[x][-1]:    # ID DAN PASSCODE SESUAI DENGAN DATABASE ADMIN
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
                        if launch_ID == data_employee[x][0] and launchPass == data_employee[x][-1]:      # ID DAN PASSCODE SESUAI DENGAN DATABASE KARYAWAN
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

    admin_column = [x[0] for x in data_admin]   # memecah data besar menjadi list-list kolom admin (menjadikan tiap data di list admin menjadi list-list terpisah)
    admin_posisi = [x[2] for x in data_admin]   # memecah data besar menjadi list-list kolom

    # MENGIMPOR DATA KARYAWAN
    data_employee = []  # VARIABEL KOSONG UNTUK MENYIMPAN DATA KARYAWAN
    with open('employee_account_database.csv') as csvfile_employee: # MEMBUKA .CSV KARYAWAN
        reader_employee = csv.reader(csvfile_employee)
        for row in reader_employee:     # menjadikan file .csv menjadi list karyawan (menambahkan tiap baris pada .csv kedalam variabel data karyawan)
            data_employee.append(row)   

    employee_column = [y[0] for y in data_employee]     # memecah data besar menjadi list-list data karyawan (menjadikan tiap data di list karyawan menjadi list-list terpisah)

    # MENGIMPOR DATA PRESENSI KARYAWAN
    data_presensi = []  # VARIABEL KOSONG UNTUK MENYIMPAN DATA PRESENSI
    with open('presensi_database.csv') as csvfile_presensi:     # MEMBUKA .CSV PRESENSI
        reader_presensi = csv.reader(csvfile_presensi)      # menjadikan file .csv menjadi list presensi (menambahkan tiap baris pada .csv kedalam variabel data presensi)
        for row in reader_presensi:
            data_presensi.append(row)

    # MENGIMPOR DATA PRESENSI ADMIN
    data_presensi_admin = []  # VARIABEL KOSONG UNTUK MENYIMPAN DATA PRESENSI
    with open('presensi_database_admin.csv') as csvfile_presensi_admin:     # MEMBUKA .CSV PRESENSI
        reader_presensi_admin = csv.reader(csvfile_presensi_admin)      # menjadikan file .csv menjadi list presensi (menambahkan tiap baris pada .csv kedalam variabel data presensi)
        for row in reader_presensi_admin:
            data_presensi_admin.append(row)

    # MENGIMPOR DATA HISTORI
    data_history = []  # VARIABEL KOSONG UNTUK MENYIMPAN DATA PRESENSI
    with open('histori_database.csv') as csvfile_histori:     # MEMBUKA .CSV PRESENSI
        reader_histori = csv.reader(csvfile_histori)      # menjadikan file .csv menjadi list presensi (menambahkan tiap baris pada .csv kedalam variabel data presensi)
        for row in reader_histori:
            data_history.append(row)

    histori_column = [y[0] for y in data_history]

    # MENGIMPOR DATA PERINTAH LEMBUR
    data_perintah_lembur = []  # VARIABEL KOSONG UNTUK MENYIMPAN DATA PERINTAH LEMBUR
    with open('perintah_lembur.csv') as csvfile_perintah_lembur:     # MEMBUKA .CSV PERINTAH
        reader_perintah_lembur = csv.reader(csvfile_perintah_lembur)      # menjadikan file .csv menjadi list perintah (menambahkan tiap baris pada .csv kedalam variabel data perintah)
        for row in reader_perintah_lembur:
            data_perintah_lembur.append(row)

    # MENGIMPOR DATA PRESENSI LEMBUR
    data_presensi_lembur = []  # VARIABEL KOSONG UNTUK MENYIMPAN DATA PRESENSI LEMBUR
    with open('employee_presensi_lembur.csv') as csvfile_presensi_lembur:     # MEMBUKA .CSV PRESENSI
        reader_presensi_lembur = csv.reader(csvfile_presensi_lembur)      # menjadikan file .csv menjadi list presensi (menambahkan tiap baris pada .csv kedalam variabel data presensi)
        for row in reader_presensi_lembur:
            data_presensi_lembur.append(row)

    # MEMBUAT DATA PENGKONDISIAN UNTUK PENGECEKAN DATA SUDAH ADA ATAU BELUM
    data_presensi_cond = [] # VARIABEL KOSONG UNTUK MENYIMPAN DATA KONDISI
    g=0 # TRIGGER BARIS KE-
    with open('presensi_database.csv') as csvfile_presensi:     # MEMBUKA .CSV PRESENSI
        reader_presensi = csv.reader(csvfile_presensi)      #menjadikan file .csv menjadi list presensi (menambahkan tiap baris pada .csv kedalam variabel data presensi)
        for row in reader_presensi:
            data_presensi_cond.append(row)
            data_presensi_cond[g][-1] = ""      # MENAMBAHKAN TIAP DATA PRESENSI KE VARIABEL KONDISI DENGAN MENGHAPUS DATA KOLOM "WAKTU"
            g+=1

    # MEMBUAT DATA PENGKONDISIAN UNTUK PENGECEKAN DATA SUDAH ADA ATAU BELUM
    data_presensi_cond_admin = [] # VARIABEL KOSONG UNTUK MENYIMPAN DATA KONDISI
    g=0 # TRIGGER BARIS KE-
    with open('presensi_database_admin.csv') as csvfile_presensi:     # MEMBUKA .CSV PRESENSI
        reader_presensi = csv.reader(csvfile_presensi)      #menjadikan file .csv menjadi list presensi (menambahkan tiap baris pada .csv kedalam variabel data presensi)
        for row in reader_presensi:
            data_presensi_cond_admin.append(row)
            data_presensi_cond_admin[g][-1] = ""      # MENAMBAHKAN TIAP DATA PRESENSI KE VARIABEL KONDISI DENGAN MENGHAPUS DATA KOLOM "WAKTU"
            g+=1


    # MENDETEKSI NAMA ADMIN MENGGUNAKAN ID
    if launch_ID in admin_column:   # ID DAN PASSCODE ADA DI DATABASE ADMIN
        for x in range(0,len(data_admin)):      # mencocokkan ID hasil login dengan ID di database
            if launch_ID == data_admin[x][0]:   # ID DAN PASSCODE SESUAI DENGAN DATABASE ADMIN
                print(f'Selamat Datang, admin "{data_admin[x][1]}"!')   # selamat datang admin

    print('Apa yang ingin anda lakukan saat ini?\n\nMenu:\n[1] PRESENSI SEKARANG!\n[2] Tambahkan Admin/Karyawan\n[3] Edit Data Admin/Karyawan\n[4] Edit Presensi Admin/Karyawan\n[5] Lihat Data\n[6] Hapus Data\n[7] KARYAWAN TERBAIK atau TERBURUK\n[8] LEMBUR\n[9] PENGGAJIAN\n[10] Keluar\n\n[N] Notifkasi')    # pilihan menu admin
    menu_choice = input("\nPilih menu : ")
    print()

    if menu_choice == '1':          # FITUR 1 PRESENSI SEKARANG

        # UI PRESENSI SEKARANG DAN PILIHAN SHIFT
        os.system('cls')
        print(f'++{'='*86}++\n|| admin>menu utama>presensi sekarang!>{' '*49}||\n++{'-'*86}++\n||{' '*86}||\n||{' '*26}P R E S E N S I   S E K A R A N G !{' '*25}||\n||{' '*86}||\n++{'='*86}++\nwaktu : {datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n\n')  

        tanggal_presensi = datetime.datetime.now().strftime("%Y-%m-%d") # INDIKATOR TANGGAL RIIL

        # HARI DALAM INDONESIA
        hari_seminggu = ["SENIN", "SELASA", "RABU", "KAMIS", "JUMAT", "SABTU", "MINGGU"]
        # MENGECEK APAKAH NAMA HARI INI
        for nomor_hari in range(3,10):
    
            # KARYAWAN YANG HENDAK PRESENSI BENAR DI SENIN-JUMAT
            if datetime.datetime.now().strftime("%A").upper() != "SATURDAY" and datetime.datetime.now().strftime("%A").upper() != "SUNDAY":  
    
                time_range = DateTimeRange(open_presensi,close_presensi)
                x = datetime.datetime.now().strftime("%H:%M:%S")    # DEKLARASI WAKTU TERBARU
                
                # BILA DALAM WAKTU GLOBAL PRESENSI
                if x in DateTimeRange(open_presensi,global_close_presensi):   # ABSENSI GLOBAL DIBUKA
                    # DALAM RENTANG PRESENSI
                    if x in time_range :    
                        status_kehadiran = "HADIR" 
                    # TIDAK DALAM RENTANG PRESENSI TAPI MASIH PADA SHIFT
                    elif x in time_range_kerja:    
                        status_kehadiran = "TERLAMBAT"
                    # PRESENSI DILUAR JAM SHIFT
                    else :          
                        input("\nPERHATIAN : Bukan jadwal presensi! Tekan [enter] untuk kembali ke menu utama")
                        status_kehadiran = "TIDAK HADIR"
                        main_page_admin()    # MENGEMBALIKAN KE MENU UTAMA
                    
                    # MEMBUAT DATA UNTUK DIMASUKKAN
                    data_baru = [tanggal_presensi, data_employee[tujuan][0], data_employee[tujuan][1], hari_seminggu[nomor_hari], status_kehadiran, now_time.strftime("%H:%M:%S")]
                    # MEMBUAT DATA PENGKONDISIAN UNTUK MENGECEK DATA SUDAH ADA ATAU BELUM
                    data_baru_cond = [f'{tanggal_presensi}', f'{data_employee[tujuan][0]}', f'{data_employee[tujuan][1]}', f'{hari_seminggu[nomor_hari]}', f'{status_kehadiran}', '']
                    
                    # MENDETEKSI APAKAH KARYAWAN SUDAH MELAKUKAN PRESENSI DI SHIFT YANG SAMA HARI INI
                    # KARYAWAN BELUM PRESENSI
                    if data_baru_cond not in data_presensi_cond_admin:    
                        data_presensi_admin.append(data_baru) # Menambahkan data baru ke dalam list data_presensi
                        with open('presensi_database_admin.csv', 'w', newline='') as csvfile_presensi:    # Membuka file CSV dalam mode penulisan dan menulis data baru ke dalamnya
                            writer_presensi = csv.writer(csvfile_presensi)
                            writer_presensi.writerows(data_presensi_admin)
                        # IN-PROGRAM-NOTIFICATION DATA DICATAT
                        input(f'\nPresensi : {tanggal_presensi},{now_time.strftime("%H:%M:%S")},{data_employee[tujuan][0]},{data_employee[tujuan][1]},{hari_seminggu[nomor_hari]},{status_kehadiran} \nPERHATIAN : Presensi berhasil direkam!\n\nTekan [enter] untuk kembali ke menu utama')   
                        main_page_admin()
                    # KARYAWAN SUDAH PRESENSI SEBELUMNYA
                    # IN-PROGRAM-NOTIFICATION DATA SUDAH ADA
                    else:
                        input(f'\nPERHATIAN : Data presensi "{tanggal_presensi},{data_employee[tujuan][0]},{data_employee[tujuan][1]},{hari_seminggu[nomor_hari]},{status_kehadiran}" sudah ada!\n\nTekan [enter] untuk kembali ke menu utama')    
                        main_page_admin()

                # ABSENSI GLOBAL BELUM DIBUKA
                elif x in pre_presensi:     
                    # MENGEMBALIKAN KE MENU UTAMA
                    input("\nPERHATIAN : Waktu belum menunjukkan jadwal presensi!\n\nTekan [enter] untuk kembali ke menu utama")
                    main_page_admin()
            
            # KARYAWAN YANG HENDAK PRESENSI BUKAN MERUPAKAN KARYAWAN SHIFT TERSEBUT
            else:   
                input("\nPERHATIAN : Bukan jadwal presensi anda! Tekan [enter] untuk melanjutkan")
                main_page_admin()

        main_page_admin()

    # FITUR 1 SELESAI UI : COMMENT : DESAIN

    elif menu_choice == '2':        # FITUR 2 TAMBAHKAN ORANG
        # PILIH MAU MENAMBAHKAN ADMIN ATAU KARYAWAN
        menu_choice_2 = input("[1] Tambahkan Admin\n[2] Tambahkan Karyawan\nPilih menu : ")
        
        if menu_choice_2 == '1':    # FITUR 2.1 TAMBAHKAN ORANG>TAMBAHKAN ADMIN
            os.system('cls')
            print(f"++{'='*86}++\n|| {f"admin>menu utama>tambahkan orang>tambahkan admin>":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*28}T A M B A H K A N   A D M I N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n\n")  # UI TAMBAHKAN ADMIN
            masukkanAdminID = input("Masukkan ID admin : ")     # ID YANG HENDAK DITAMBAHKAN

            # MENDETEKSI APAKAH DATA ID SUDAH ADA
            if masukkanAdminID not in admin_column:     # BILA ID YANG HENDAK DITAMBAHKAN BELUM ADA
                
                # LIST POSISI
                Posisi = [["CPO"],["CEO"],["CFO"],["COO"],["CMO"],["CPO"],["CTO"]]
                # MENJADIKAN LIST DIPRINT HORIZONTAL INSTEAD OF VERTIKAL
                Posisi_horizontal = [pos[0] for pos in Posisi]
                tabel_posisi = [Posisi_horizontal]
                print(tabulate.tabulate(tabel_posisi, tablefmt=kolom_fmt))

                masukkanAdminPosisi  = input("Masukkan posisi admin : ").upper()
                # BILA POSISI ADMIN KOSONG
                if masukkanAdminPosisi not in admin_posisi:
                    masukkanAdminNama    = input("Masukkan nama admin : ")
                    masukkanAdminPass    = input("Masukkan passcode admin (case sensitive) : ")
                    # MEMBUAT DATA YANG AKAN DIMASUKKAN
                    masukan_tambah_admin = [masukkanAdminID.upper(),masukkanAdminNama.upper(),masukkanAdminPosisi.upper(),masukkanAdminPass]
                    # MEMASUKKAN DATA KE LIST 
                    data_admin.append(masukan_tambah_admin)
                    # MEMBUKA .CSV DAN MEMASUKKAN DATA
                    with open('admin_account_database.csv', 'w', newline='') as csvfile_admin:
                        writer_admin = csv.writer(csvfile_admin)
                        writer_admin.writerows(data_admin)
                    # NOTIFIKASI DATA BERHASIL DIMASUKKAN
                    input(f'\nData baru : {masukkanAdminID.upper()},{masukkanAdminNama.upper()},{masukkanAdminPosisi.upper()},{masukkanAdminPass}\nPERHATIAN : Data admin berhasil ditambahkan!\n\nTekan [enter] untuk kembali ke menu utama')    # IN-PROGRAM-NOTIFIKASI BAHWA DATA ADMIN BARU BERHASIL DITAMBAHKAN
                # BILA POSISI ADMIN SUDAH ADA
                else :
                    input(f'\nPERHATIAN : Data admin "{masukkanAdminPosisi}" sudah ada!\nTekan [enter] untuk kembali ke menu utama')

            # BILA ID YANG HENDAK DITAMBAHKAN SUDAH ADA
            else:
                input(f'\nPERHATIAN : Data admin "{masukkanAdminID}" sudah ada!\n\nTekan [enter] untuk kembali ke menu utama')

            main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN

        # FITUR 2.1 SELESAI UI : COMMENT : DESAIN

        elif menu_choice_2 == '2':  # FITUR 2.2 TAMBAHKAN ORANG>TAMBAHKAN KARYAWAN
            os.system('cls')
            print(f"++{'='*86}++\n|| {f"admin>menu utama>tambahkan orang>tambahkan karyawan>":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*25}T A M B A H K A N   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n\n")    # UI TAMBAHKAN KARYAWAN

            masukkanKaryawanID = input("Masukkan ID karyawan : ")

            # BILA ID TIDAK DITEMUKAN DI DB EMPLOYEE
            if masukkanKaryawanID not in [employee[0] for employee in data_employee]:
                # LIST POSISI
                Posisi = [["Sekretaris"],["Akuntan"],["Sales Representative"],["Tax"],["Cs"],["Admin"],["Hr"],["Digital Marketing"],["Designer"],["Pm"],["Developer"],["Data Analyst"]]
                # MENJADIKAN LIST DIPRINT HORIZONTAL INSTEAD OF VERTIKAL
                Posisi_horizontal = [pos[0].upper() for pos in Posisi]
                tabel_posisi = [Posisi_horizontal]
                print(tabulate.tabulate(tabel_posisi, tablefmt=kolom_fmt))

                masukkanKaryawanPosisi = input("Masukkan posisi karyawan: ")

                masukkanKaryawanNama = input("Masukkan nama karyawan : ")
                masukkanKaryawanPass = input("Masukkan passcode karyawan (case sensitive) : ")

                # MEMBUAT DATA BARU
                masukan_tambah_karyawan = [masukkanKaryawanID.upper(), masukkanKaryawanNama.upper(), masukkanKaryawanPosisi.upper(), masukkanKaryawanPass]
                # MEMASUKKAN DATA BARU KE LIST
                data_employee.append(masukan_tambah_karyawan)
                # MEMBUKA .CSV DAN MEMASUKKAN LIST
                with open('employee_account_database.csv', 'w', newline='') as csvfile_employee:
                    writer_employee = csv.writer(csvfile_employee)
                    writer_employee.writerows(data_employee)
                # NOTIFIKASI DATA BERHASIL DITAMBAHKAN
                input(f'\nData baru : {masukkanKaryawanID.upper()},{masukkanKaryawanNama.upper()},{masukkanKaryawanPosisi.upper()},{masukkanKaryawanPass}\nPERHATIAN : Data karyawan berhasil ditambahkan!\n\nTekan [enter] untuk kembali ke menu utama')
            
            # BILA ID DITEMUKAN SUDAH ADA DI DB
            else:
                input(f'\nPERHATIAN : Data karyawan "{masukkanKaryawanID}" sudah ada!\n\nTekan [enter] untuk kembali ke menu utama')

            main_page_admin()

        # FITUR 2.2 SELESAI UI : COMMENT : DESAIN

        else:                       # FITUR 2.3 BILA SALAH KEMBALI KE MENU UTAMA KARYAWAN
            main_page_admin()

        # FITUR 2.3 SELESAI - UI : COMMENT : DESAIN

    # FITUR 2 SELESAI  UI : COMMENT : DESAIN

    elif menu_choice == '3':        # FITUR 3 EDIT DATA 
        #  PILIH HENDAK MENGUBAH DATA ADMIN ATAU KARYAWAN
        menu_choice_3 = input("[1] Edit Data Admin\n[2] Edit Data Karyawan\nPilih menu : ")

        if menu_choice_3 == '1':    # FITUR 3.1 EDIT DATA>EDIT DATA ADMIN
            os.system('cls')
            # MENGUBAH LIST MENJADI TABEL DENGAN PANDAS
            df = pd.DataFrame(data_admin, columns=kolom_admin)
            # SORTING MENGGUNAKAN METHOD
            df.sort_values(by='ID', inplace=True)
            # UI ADMIN DAN INPUTAN ADMIN MANA YANG HENDAK DIEDIT
            masukan_edit_admin = input(f"++{'='*86}++\n|| {f'admin>menu utama>edit data>edit data admin>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*28}E D I T   D A T A   A D M I N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('%A, %d %B %Y | %H:%M:%S')}\n\n\ndata saat ini:\n\n{tabulate.tabulate(df, headers='keys', tablefmt=kolom_fmt, showindex=False)}\n\nMasukkan ID admin yang hendak diubah : ")

            # MENDETEKSI DATA ID YANG HENDAK DIUBAH ADA : BINARY SEARCH
            low, high = 0, len(df) - 1
            index_admin = -1
            while low <= high:  # LOGIKA BINARY SEARCH
                mid = (low + high) // 2
                if df.iloc[mid]['ID'] == masukan_edit_admin:
                    index_admin = mid
                    break
                elif df.iloc[mid]['ID'] < masukan_edit_admin:
                    low = mid + 1
                else:
                    high = mid - 1
            
            # BILA ID YANG HENDAK DIUBAH ITU ADA
            if index_admin != -1:
                # DARI DATA ID DIPANGGIL DATA FULL SATU BARISNYA
                baris_admin = df.iloc[index_admin]
                # NOTIFIKASI DATA YANG HENDAK DIEDIT
                header = list(baris_admin.index)
                values = list(baris_admin.values)
                table = [header, values]
                os.system('cls')
                print(f"++{'='*86}++\n|| {f'admin>menu utama>edit data>edit data admin>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*28}E D I T   D A T A   A D M I N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('%A, %d %B %Y | %H:%M:%S')}\n")
                print(f"Data yang akan diedit : \n{tabulate.tabulate(table, headers='firstrow', tablefmt=kolom_fmt)}\nMasukkan [enter] untuk melewati pengeditan\n")
                
                # MEMASUKKAN IDENTITAS BARU
                IDBaru = input("Masukkan ID baru      : ")

                # LIST POSISI
                Posisi = [["CPO"],["CEO"],["CFO"],["COO"],["CMO"],["CPO"],["CTO"]]
                # MENJADIKAN LIST DIPRINT HORIZONTAL INSTEAD OF VERTIKAL
                Posisi_horizontal = [pos[0] for pos in Posisi]
                tabel_posisi = [Posisi_horizontal]
                print(tabulate.tabulate(tabel_posisi, tablefmt=kolom_fmt))

                posisiBaru = input("Masukkan posisi baru  : ").upper()

                # BILA POSISI KOSONG
                if posisiBaru not in admin_posisi:
                    namaBaru = input("Masukkan nama baru    : ")
                    passBaru = input("Masukkan passcode baru: ")

                    # LOGIKA INPUTAN DATA BARU : BILA '' MAKA SKIP, BILA TIDAK MAKA AKAN DI-REPLACE

                    # ID
                    if IDBaru == '':    # SKIP
                        pass
                    else:               # REPLACE
                        df.at[index_admin, 'ID'] = IDBaru.upper()
                    # NAMA
                    if namaBaru == '':  # SKIP
                        pass
                    else:               # REPLACE
                        df.at[index_admin, 'Nama'] = namaBaru.upper()
                    # POSISI
                    if posisiBaru == '':    #SKIP
                        pass
                    else:                   # REPLACE
                        df.at[index_admin, 'Posisi'] = posisiBaru.upper()
                    # PASSCODE
                    if passBaru == '':  # SKIP
                        pass
                    else:               # REPLACE
                        df.at[index_admin, 'Passcode'] = passBaru
                    
                    # MENYIMPAN DATA BARU KE DATABASE
                    np.savetxt('admin_account_database.csv', df, delimiter=',', fmt='%s')
                    # NOTIFIKASI DATA BERHASIL DIUBAH
                    os.system('cls')
                    print(f"++{'='*86}++\n|| {f'admin>menu utama>edit data>edit data admin>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*28}E D I T   D A T A   A D M I N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('%A, %d %B %Y | %H:%M:%S')}\n\nData baru \"{masukan_edit_admin}\" telah diubah!\n\nData saat ini :\n{tabulate.tabulate(df, headers="keys", tablefmt=kolom_fmt, showindex=False)}\n")
                # BILA POSISI SUDAH ADA DI DB
                else:
                    print(f'\nPERHATIAN : Data admin "{posisiBaru}" sudah ada!\n')

            # DATA YANG HENDAK DIUBAH TIDAK ADA
            else:
                print(f'PERHATIAN : "{masukan_edit_admin}" tidak ada dalam database!')
            
            # MENGEMBALIKAN KE MENU UTAMA ADMIN
            input("Tekan [enter] untuk kembali ke menu utama")
            main_page_admin()

        # FITUR 3.1 SELESAI : UI : COMMENT : DESAIN

        elif menu_choice_3 == '2':        # FITUR 3.2 EDIT DATA KARYAWAN 
            os.system('cls')
            # MENGUBAH LIST MENJADI TABEL DENGAN PANDAS
            df = pd.DataFrame(data_employee, columns=kolom_employee)
            # SORTING ID MENGGUNAKAN METHOD
            df.sort_values(by='ID', inplace=True)
            # UI DAN INPUT ID MANA YANG HENDAK DIUBAH
            masukan_edit_employee = input(f"++{'='*86}++\n|| {f'admin>menu utama>edit data>edit data karyawan>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*25}E D I T   D A T A   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('%A, %d %B %Y | %H:%M:%S')}\n\n\n\n{tabulate.tabulate(df, headers='keys', tablefmt=kolom_fmt, showindex=False)}\n\nMasukkan ID karyawan yang hendak diubah : ")
            
            # MENDETEKSI DATA ID YANG HENDAK DIUBAH ADA : BINARY SEARCH
            low, high = 0, len(df) - 1
            index_employee = -1
            while low <= high:  # LOGIKA BINARY SEARCH
                mid = (low + high) // 2
                if df.iloc[mid]['ID'] == masukan_edit_employee:
                    index_employee = mid
                    break
                elif df.iloc[mid]['ID'] < masukan_edit_employee:
                    low = mid + 1
                else:
                    high = mid - 1

            # BILA ID YANG HENDAK DIUBAH ITU ADA
            if index_employee != -1:
                # DARI ID DIPANGGIL DATA SATU BARIS PENUHNYA
                baris_employee = df.iloc[index_employee]
                # NOTIFIKASI DATA YANG HENDAK DIEDIT
                print(f"\nData yang akan diedit : \n{baris_employee.to_string(index=False, header=False)}\nMasukkan [enter] untuk melewati pengeditan\n") 
                
                # MEMASUKKAN IDENTITAS BARU
                IDBaru     = input("Masukkan ID baru      : ")
                namaBaru   = input("Masukkan nama baru    : ")
                posisiBaru = input("Masukkan posisi baru  : ")
                passBaru   = input("Masukkan passcode baru: ")

                # LOGIKA INPUTAN DATA BARU : BILA '' MAKA SKIP, BILA TIDAK MAKA AKAN DI-REPLACE

                # ID
                if IDBaru == '':    # SKIP
                    pass
                else:               # REPLACE
                    df.at[index_employee, 'ID'] = IDBaru.upper()
                # NAMA
                if namaBaru == '':  # SKIP
                    pass
                else:               # REPLACE
                    df.at[index_employee, 'Nama'] = namaBaru.upper()
                # POSISI
                if posisiBaru == '':    # SKIP
                    pass
                else:                   # REPLACE
                    df.at[index_employee, 'Posisi'] = posisiBaru.upper()
                # PASSCODE
                if passBaru == '':  # SKIP
                    pass
                else:               # REPLACE
                    df.at[index_employee, 'Passcode'] = passBaru
                
                # MENYIMPAN DATA BARU KE DATABASE
                np.savetxt('employee_account_database.csv', df, delimiter=',', fmt='%s')
                # IN-PROGRAM-NOTIFICATION DATA BERHASIL DIUBAH
                print(f'\nData baru untuk "{df.iloc[index_employee].to_string(header=False, index=False)}" telah diubah!\n\nData saat ini :\n{tabulate.tabulate(df, headers="keys", tablefmt=kolom_fmt, showindex=False)}\n')

            # DATA YANG HENDAK DIUBAH TIDAK ADA
            else:   
                input("PERHATIAN : Kesalahan input atau data tidak ada...")    

            input("\nTekan [enter] untuk kembali ke menu utama")
            main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN

        # FITUR 3.2 SELESAI : UI : COMMENT : DESAIN

    # FITUR 3 SELESAI : UI : COMMENT : DESAIN

    elif menu_choice == '4':        # FITUR 4 EDIT DATA PRESENSI
        os.system('cls')
        # MENGUBAH LIST MENJADI TABEL DENGAN PANDAS
        df = pd.DataFrame(data_presensi_admin, columns=kolom_presensi)    
        print(f"++{'='*86}++\n|| {f"admin>menu utama>edit presensi >":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*31}E D I T   P R E S E N S I ':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('\r%A, %d %B %Y | %H:%M:%S')}\n")
        # PILIH HENDAK MENGAKSES MENU EDIT ADMIN ATAU KARYAWAN
        edit_choice = input("\n[1] Edit Presensi Admin\n[2] Edit Presensi Karyawan\n\n[3 atau lainnya] Kembali ke Menu Utama\n\nPilih menu : ")

        if edit_choice == '1':      # FITUR 4.1 EDIT DATA PRESENSI>EDIT PRESENSI ADMIN
            os.system('cls')
            print(F"++{'='*86}++\n|| {f"admin>menu utama>edit presensi>edit presensi admin>":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*25}E D I T   P R E S E N S I   A D M I N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('\r%A, %d %B %Y | %H:%M:%S')}\n")
            # MENAMPILKAN SELURUH DATA ADMIN
            print(tabulate.tabulate(data_admin, headers=kolom_employee, tablefmt=kolom_fmt, showindex=False)) 
            # INPUT ID ADMIN MANA YANG HENDAK DIEDIT
            masukan_edit_presensi_id = input("\nMasukkan ID admin yang hendak diubah : ")

            # BILA DATA YANG HENDAK DIUBAH ITU ADA
            if masukan_edit_presensi_id in df['ID'].values:     
                # MENCARI DATA YANG MEMILIKI ISI YANG SESUAI
                masukan_edit_presensi_tanggal = input("Masukkan tanggal yang dicari : ")    
                # FILTRASI DATA PANDAS YANG SESUAI DENGAN ID
                filtered_df = df.loc[df['ID'].str.contains(masukan_edit_presensi_id)]   # FILTRASI ID SESUAI
                filtered_df = filtered_df.loc[df['Tanggal'].str.contains(masukan_edit_presensi_tanggal)]    # FILTRASI TANGGAL SESUAI
                
                # BILA HASIL FILTRASI TIDAK ADA (DATA YANG DICARI TIDAK ADA)
                if len(filtered_df) == 0 :
                    print("\nPERHATIAN : Data yang anda cari tidak ditemukan...\n")
                # BILA HASIL FILTRASI ADA (DATA YANG DICARI ADA)
                else :
                    try:
                        os.system('cls')
                        print(F"++{'='*86}++\n|| {f"admin>menu utama>edit presensi>edit presensi admin>":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*25}E D I T   P R E S E N S I   A D M I N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('\r%A, %d %B %Y | %H:%M:%S')}\n")
                        print(f'\nHasil pencarian :\n\n{tabulate.tabulate(filtered_df, headers="keys", tablefmt=kolom_fmt)}')
                        # KONFIRMASI DATA PRESENSI YANG HENDAK DIEDIT
                        masukan_edit_presensi_index = int(input("\nPilih index yang akan diedit: "))    

                        # MENCOCOKKAN INDEX DATA YANG ADA DENGAN INDEX DATA YANG HENDAK DIEDIT
                        # BILA INDEX DIMASUKKAN ADA
                        if masukan_edit_presensi_index == filtered_df.index :
                            os.system('cls')
                            print(F"++{'='*86}++\n|| {f"admin>menu utama>edit presensi>edit presensi admin>":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*25}E D I T   P R E S E N S I   A D M I N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('\r%A, %d %B %Y | %H:%M:%S')}\n")
                            print(f"\nData yang akan diedit : \n{tabulate.tabulate((df[masukan_edit_presensi_index:masukan_edit_presensi_index+1]), headers="keys", tablefmt=kolom_fmt, showindex=False)}\n\nTekan [enter] untuk melewati perubahan\n")  # KONFIRMASI PENGEDITAN

                            # INPUTAN DATA
                            masukanEditPresensiTanggalBaru = input("Masukkan tanggal baru : ")  
                            masukanEditPresensiIDBaru      = input("Masukkan ID baru      : ")
                            masukanEditPresensiNamaBaru    = input("Masukkan Nama baru    : ") 
                            masukanEditPresensiHariBaru    = input("Masukkan Hari baru    : ")
                            masukanEditPresensiStatusBaru  = input("Masukkan Status kehadiran baru : ")
                            masukanEditPresensiWaktuBaru   = input("Masukkan waktu baru   : ")
                            
                            # LOGIKA INPUTAN DATA BARU : BILA '' MAKA SKIP, BILA TIDAK MAKA AKAN DI-REPLACE

                            # TANGGAL
                            if masukanEditPresensiTanggalBaru == '':# SKIP
                                pass
                            else:                                   # REPLACE
                                df.iloc[masukan_edit_presensi_index, 0] = masukanEditPresensiTanggalBaru.upper()
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
                            # HARI
                            if masukanEditPresensiHariBaru == '': #SKIP
                                pass
                            else:                                   # REPLACE
                                df.iloc[masukan_edit_presensi_index, 3] = masukanEditPresensiStatusBaru.upper()
                            # STATUS KEHADIRAN
                            if masukanEditPresensiStatusBaru == '': #SKIP
                                pass
                            else:                                   # REPLACE
                                df.iloc[masukan_edit_presensi_index, 4] = masukanEditPresensiStatusBaru.upper()
                            # WAKTU
                            if masukanEditPresensiWaktuBaru == '':  # SKIP
                                pass
                            else:                                   # REPLACE
                                df.iloc[masukan_edit_presensi_index, 5] = masukanEditPresensiWaktuBaru.upper()

                            # MENYIMPAN DATA BARU KE DATABASE
                            np.savetxt('presensi_database_admin.csv',df,delimiter=',',fmt='%s')
                            # IN-PROGRAM-NOTIFICATION DATA BERHASIL DIUBAH
                            print(f'\nData baru "{masukan_edit_presensi_id}" telah diubah!\n\nData saat ini :\n{tabulate.tabulate((df[masukan_edit_presensi_index:masukan_edit_presensi_index+1]), headers="keys", tablefmt=kolom_fmt, showindex=False)}\n') 
                        
                        # INDEX MASUKAN TIDAK COCOK DENGAN YANG HENDAK DIUBAH
                        else:
                            print("PERHATIAN : Input anda tidak dalam range yang hendak diedit!\n")
                    except:
                        print("PERHATIAN : format input yang anda cari tidak tepat")

            # DATA YANG HENDAK DIUBAH TIDAK ADA
            else:
                print(f"PERHATIAN : {masukan_edit_presensi_id} tidak ada dalam database.")

        # FITUR 4.1 SELESAI : UI :COMMENT : DESAIN

        elif edit_choice == '2':    # FITUR 4.2 EDIT DATA PRESENSI>EDIT PRESENSI KARYAWAN
            os.system('cls')
            print(F"++{'='*86}++\n|| {f"admin>menu utama>edit presensi>edit presensi karyawan>":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*21}E D I T   P R E S E N S I   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('\r%A, %d %B %Y | %H:%M:%S')}\n")
            # MENAMPILKAN SELURUH DATA KARYAWAN
            print(tabulate.tabulate(data_employee, headers=kolom_employee, tablefmt=kolom_fmt, showindex=False)) 
            # INPUT ID KARYAWAN MANA YANG HENDAK DIEDIT
            masukan_edit_presensi_id = input("\nMasukkan ID karyawan yang hendak diubah : ")

            # BILA DATA YANG HENDAK DIUBAH ITU ADA
            if masukan_edit_presensi_id in df['ID'].values:     
                # MENCARI DATA YANG MEMILIKI ISI YANG SESUAI
                masukan_edit_presensi_tanggal = input("Masukkan tanggal yang dicari : ")    
                # FILTRASI DATA PANDAS YANG SESUAI DENGAN ID
                filtered_df = df.loc[df['ID'].str.contains(masukan_edit_presensi_id)]   # FILTRASI ID SESUAI
                filtered_df = filtered_df.loc[df['Tanggal'].str.contains(masukan_edit_presensi_tanggal)]    # FILTRASI TANGGAL SESUAI
                
                # BILA HASIL FILTRASI TIDAK ADA (DATA YANG DICARI TIDAK ADA)
                if len(filtered_df) == 0 :
                    print("\nPERHATIAN : Data yang anda cari tidak ditemukan...\n")
                # BILA HASIL FILTRASI ADA (DATA YANG DICARI ADA)
                else :
                    try:
                        os.system('cls')
                        print(F"++{'='*86}++\n|| {f"admin>menu utama>edit presensi>edit presensi karyawan>":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*21}E D I T   P R E S E N S I   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('\r%A, %d %B %Y | %H:%M:%S')}\n")
                        print(f'\nHasil pencarian :\n\n{tabulate.tabulate(filtered_df, headers="keys", tablefmt=kolom_fmt)}')
                        # KONFIRMASI DATA PRESENSI YANG HENDAK DIEDIT
                        masukan_edit_presensi_index = int(input("\nPilih index yang akan diedit: "))    

                        # MENCOCOKKAN INDEX DATA YANG ADA DENGAN INDEX DATA YANG HENDAK DIEDIT
                        # BILA INDEX DIMASUKKAN ADA
                        if masukan_edit_presensi_index == filtered_df.index :
                            os.system('cls')
                            print(F"++{'='*86}++\n|| {f"admin>menu utama>edit presensi>edit presensi karyawan>":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*21}E D I T   P R E S E N S I   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('\r%A, %d %B %Y | %H:%M:%S')}\n")
                            print(f"\nData yang akan diedit : \n{tabulate.tabulate((df[masukan_edit_presensi_index:masukan_edit_presensi_index+1]), headers="keys", tablefmt=kolom_fmt, showindex=False)}\n\nTekan [enter] untuk melewati perubahan\n")  # KONFIRMASI PENGEDITAN

                            # INPUTAN DATA
                            masukanEditPresensiTanggalBaru = input("Masukkan tanggal baru : ")  
                            masukanEditPresensiIDBaru      = input("Masukkan ID baru      : ")
                            masukanEditPresensiNamaBaru    = input("Masukkan Nama baru    : ") 
                            masukanEditPresensiHariBaru    = input("Masukkan Hari baru    : ")
                            masukanEditPresensiStatusBaru  = input("Masukkan Status kehadiran baru : ")
                            masukanEditPresensiWaktuBaru   = input("Masukkan waktu baru   : ")
                            
                            # LOGIKA INPUTAN DATA BARU : BILA '' MAKA SKIP, BILA TIDAK MAKA AKAN DI-REPLACE

                            # TANGGAL
                            if masukanEditPresensiTanggalBaru == '':# SKIP
                                pass
                            else:                                   # REPLACE
                                df.iloc[masukan_edit_presensi_index, 0] = masukanEditPresensiTanggalBaru.upper()
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
                            # HARI
                            if masukanEditPresensiHariBaru == '': #SKIP
                                pass
                            else:                                   # REPLACE
                                df.iloc[masukan_edit_presensi_index, 3] = masukanEditPresensiStatusBaru.upper()
                            # STATUS KEHADIRAN
                            if masukanEditPresensiStatusBaru == '': #SKIP
                                pass
                            else:                                   # REPLACE
                                df.iloc[masukan_edit_presensi_index, 4] = masukanEditPresensiStatusBaru.upper()
                            # WAKTU
                            if masukanEditPresensiWaktuBaru == '':  # SKIP
                                pass
                            else:                                   # REPLACE
                                df.iloc[masukan_edit_presensi_index, 5] = masukanEditPresensiWaktuBaru.upper()

                            # MENYIMPAN DATA BARU KE DATABASE
                            np.savetxt('presensi_database.csv',df,delimiter=',',fmt='%s')
                            # IN-PROGRAM-NOTIFICATION DATA BERHASIL DIUBAH
                            print(f'\nData baru "{masukan_edit_presensi_id}" telah diubah!\n\nData saat ini :\n{tabulate.tabulate((df[masukan_edit_presensi_index:masukan_edit_presensi_index+1]), headers="keys", tablefmt="github", showindex=False)}\n') 
                        
                        # INDEX MASUKAN TIDAK COCOK DENGAN YANG HENDAK DIUBAH
                        else:
                            print("PERHATIAN : Input anda tidak dalam range yang hendak diedit!\n")
                    except:
                        print("PERHATIAN : format input yang anda cari tidak tepat")

            # DATA YANG HENDAK DIUBAH TIDAK ADA
            else:
                print(f"PERHATIAN : {masukan_edit_presensi_id} tidak ada dalam database.")

        # FITUR 4.2 SELESAI : UI :COMMENT : DESAIN

        else :
            main_page_admin()

        input("Tekan [enter] untuk kembali ke Menu Utama") 
        main_page_admin()
    
    # FITUR 4 SELESAI : UI : COMMENT : DESAIN

    elif menu_choice == '5':        # FITUR 5 LIHAT DATA
        menu_choice_5 = input("[1] Lihat Data Admin\n[2] Lihat Data Karyawan\n[3] Lihat Presensi Admin\n[4] Lihat Presensi Karyawan\n[enter] Kembali ke menu utama\n\nPilih menu : ")

        if menu_choice_5 == '1':    # FITUR 5.1 LIHAT DATA>LIHAT DATA ADMIN
            os.system('cls')
            print(f"++{'='*86}++\n|| {f'admin>menu utama>lihat data>lihat data admin>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*27}L I H A T   D A T A   A D M I N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('\r%A, %d %B %Y | %H:%M:%S')}\n")

            # MENAMPILKAN DATA
            df = pd.DataFrame(data_admin, columns=kolom_admin)    # MEMASUKKAN LIST DATA BESAR KE PANDAS

            # ALGORITMA MERGE SORT
            def merge_sort(df, column):
                if len(df) > 1:
                    mid = len(df) // 2
                    left_half = df.iloc[:mid].copy()
                    right_half = df.iloc[mid:].copy()

                    merge_sort(left_half, column)
                    merge_sort(right_half, column)

                    i = j = k = 0

                    while i < len(left_half) and j < len(right_half):
                        if left_half.iloc[i][column] < right_half.iloc[j][column]:
                            df.iloc[k] = left_half.iloc[i]
                            i += 1
                        else:
                            df.iloc[k] = right_half.iloc[j]
                            j += 1
                        k += 1

                    while i < len(left_half):
                        df.iloc[k] = left_half.iloc[i]
                        i += 1
                        k += 1

                    while j < len(right_half):
                        df.iloc[k] = right_half.iloc[j]
                        j += 1
                        k += 1
            # MELAKUKAN SORTING MENGGUNAKAN ALGORITMA MERGE SORT
            merge_sort(df, 'ID')

            # DISPLAY TABEL
            print(tabulate.tabulate(df.iloc[:, :2], headers="keys", tablefmt=kolom_fmt, showindex=False))
                
            # FITUR SEARCH BERDASARKAN ID
            search_ID = str(input("\nMasukkan ID yang hendak dicari : "))
                
            # MENCARI BERDASARKAN ID : BINARY SEARCH
            left, right = 0, len(df) - 1
            hasil_pencarian = None
                
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
                
            # BILA DATA DITEMUKAN
            if hasil_pencarian is not None:
                os.system('cls')
                print(f"++{'='*86}++\n|| {f'admin>menu utama>lihat data>lihat data admin>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*27}L I H A T   D A T A   A D M I N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('\r%A, %d %B %Y | %H:%M:%S')}\n")
                # MEMUNCULKAN DATA YANG DITEMUKAN
                print("Data Admin Ditemukan:")
                table = [[hasil_pencarian['ID'], hasil_pencarian['Nama'], hasil_pencarian['Posisi'], hasil_pencarian['Password']]]
                print(tabulate.tabulate(table, headers=kolom_admin, tablefmt=kolom_fmt))
            # BILA DATA TIDAK DITEMUKAN
            else:
                print("PERHATIAN : Admin dengan ID tersebut tidak ditemukan.")
                
            input("\nTekan [enter] untuk kembali ke menu utama") 

        # FITUR 5.1 SELESAI : UI : COMMENT : DESAIN

        elif menu_choice_5 == '2':    # FITUR 5.2 LIHAT DATA>LIHAT DATA KARYAWAN
            os.system('cls')
            print(f"++{'='*86}++\n|| {f'admin>menu utama>lihat data>lihat data karyawan>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*24}L I H A T   D A T A   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('\r%A, %d %B %Y | %H:%M:%S')}\n")
                
            # MENAMPILKAN DATA
            df = pd.DataFrame(data_employee, columns=kolom_employee)    # MEMASUKKAN LIST DATA BESAR KE PANDAS

            # ALGORITMA MERGE SORT
            def merge_sort(df, column):
                if len(df) > 1:
                    mid = len(df) // 2
                    left_half = df.iloc[:mid].copy()
                    right_half = df.iloc[mid:].copy()

                    merge_sort(left_half, column)
                    merge_sort(right_half, column)

                    i = j = k = 0

                    while i < len(left_half) and j < len(right_half):
                        if left_half.iloc[i][column] < right_half.iloc[j][column]:
                            df.iloc[k] = left_half.iloc[i]
                            i += 1
                        else:
                            df.iloc[k] = right_half.iloc[j]
                            j += 1
                        k += 1

                    while i < len(left_half):
                        df.iloc[k] = left_half.iloc[i]
                        i += 1
                        k += 1

                    while j < len(right_half):
                        df.iloc[k] = right_half.iloc[j]
                        j += 1
                        k += 1
            # MELAKUKAN SORTING MENGGUNAKAN ALGORITMA MERGE SORT
            merge_sort(df, 'ID')

            # DISPLAY TABEL
            print(tabulate.tabulate(df.iloc[:, :2], headers="keys", tablefmt=kolom_fmt, showindex=False))
                
            # FITUR SEARCH BERDASARKAN ID
            search_ID = str(input("\nMasukkan ID yang hendak dicari : "))
                
            # MENCARI BERDASARKAN ID : BINARY SEARCH
            left, right = 0, len(df) - 1
            hasil_pencarian = None
                
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
                
            # BILA DATA DITEMUKAN
            if hasil_pencarian is not None:
                os.system('cls')
                print(f"++{'='*86}++\n|| {f'admin>menu utama>lihat data>lihat data karyawan>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*24}L I H A T   D A T A   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('\r%A, %d %B %Y | %H:%M:%S')}\n")
                # MEMUNCULKAN DATA YANG DITEMUKAN
                print("Data Karyawan Ditemukan:")
                table = [[hasil_pencarian['ID'], hasil_pencarian['Nama'], hasil_pencarian['Posisi'], hasil_pencarian['Password']]]
                print(tabulate.tabulate(table, headers=kolom_employee, tablefmt=kolom_fmt))
            # BILA DATA TIDAK DITEMUKAN
            else:
                print("PERHATIAN : Karyawan dengan ID tersebut tidak ditemukan.")
                
            input("\nTekan [enter] untuk kembali ke menu utama") 

        # FITUR 5.2 SELESAI : UI : COMMENT : DESAIN

        elif menu_choice_5 == '3':    # FITUR 5.3 LIHAT DATA>LIHAT PRESENSI ADMIN
            os.system('cls')
            print(f"++{'='*86}++\n|| {f'admin>menu utama>lihat data>lihat presensi admin>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*24}L I H A T   P R E S E N S I   A D M I N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('\r%A, %d %B %Y | %H:%M:%S')}\n")

            # MENAMPILKAN DATA
            df = pd.DataFrame(data_admin, columns=kolom_admin)    # MEMASUKKAN LIST DATA BESAR KE PANDAS

            # ALGORITMA MERGE SORT
            def merge_sort(df, column):
                if len(df) > 1:
                    mid = len(df) // 2
                    left_half = df.iloc[:mid].copy()
                    right_half = df.iloc[mid:].copy()

                    merge_sort(left_half, column)
                    merge_sort(right_half, column)

                    i = j = k = 0

                    while i < len(left_half) and j < len(right_half):
                        if left_half.iloc[i][column] < right_half.iloc[j][column]:
                            df.iloc[k] = left_half.iloc[i]
                            i += 1
                        else:
                            df.iloc[k] = right_half.iloc[j]
                            j += 1
                        k += 1

                    while i < len(left_half):
                        df.iloc[k] = left_half.iloc[i]
                        i += 1
                        k += 1

                    while j < len(right_half):
                        df.iloc[k] = right_half.iloc[j]
                        j += 1
                        k += 1
            # MELAKUKAN SORTING MENGGUNAKAN ALGORITMA MERGE SORT
            merge_sort(df, 'ID')
            # DISPLAY TABEL
            print(tabulate.tabulate(df.iloc[:, :2], headers="keys", tablefmt=kolom_fmt, showindex=False))

            df = pd.DataFrame(data_presensi_admin, columns=kolom_presensi) 
            df = df.sort_values(by='ID', ascending=True)  # Sortir berdasarkan ID
            # FITUR SEARCH BERDASARKAN ID
            search_ID = input("\nMasukkan ID yang hendak dilihat : ")

            # BINARY SEARCH
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
                menu_presensi_admin = input("Menu :\n[1] Lihat Data Presensi\n[2] Lihat Rekapitulasi Presensi\nMasukan opsi : ")

                if menu_presensi_admin == '1':       # FITUR 5.3.1 LIHAT DATA>LIHAT PRESENSI ADMIN>LIHAT DATA PRESENSI
                    os.system('cls')
                    print(f"++{'='*86}++\n|| {f'admin>menu utama>lihat data>lihat presensi admin>cari ID>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*24}L I H A T   P R E S E N S I   A D M I N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('\r%A, %d %B %Y | %H:%M:%S')}")

                    filtered_df = df.iloc[[index]]  # deklarasi data hasil filter
                    print(f'\nHasil Pencarian untuk ID "{search_ID}"\n')
                    print(tabulate.tabulate(filtered_df, headers='keys', tablefmt=kolom_fmt, showindex=False))

                    # SEARCHING LAGI DENGAN TANGGAL
                    search_date = input("\nMasukkan Tanggal yang hendak dicari [yyyy-mm-dd] : ")

                    if search_date in filtered_df['Tanggal'].values:  # SEARCHING ADA DI DATABASE
                        os.system('cls')
                        print(f"++{'='*86}++\n|| {f'admin>menu utama>lihat data>lihat presensi admin>cari ID>cari tanggal>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*24}L I H A T   P R E S E N S I   A D M I N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('\r%A, %d %B %Y | %H:%M:%S')}\n")

                        filtered_df = filtered_df.loc[filtered_df['Tanggal'].str.contains(search_date)]
                        print(f'\nHasil Pencarian untuk tanggal "{search_date}"\n')
                        print(tabulate.tabulate(filtered_df, headers='keys', tablefmt=kolom_fmt, showindex=False))
                    else:  # HASIL SEARCHING DENGAN TANGGAL TIDAK DITEMUKAN
                        print("\nData yang anda cari tidak ada...")
                    
                    input("\nTekan [enter] untuk kembali ke menu utama")
                
                elif menu_presensi_admin == '2':     # FITUR 5.3.2 LIHAT DATA>LIHAT PRESENSI ADMIN>LIHAT REKAPITULASI PRESENSI ADMIN
                    
                    # FILTER DF BERDASARKAN ID YANG DICARI
                    filtered_df = df.loc[df['ID'] == search_ID]

                    # PILIHAN REKAP
                    ulangAdmin4 = True
                    while ulangAdmin4:
                        os.system('cls')
                        print(f"++{'='*86}++\n|| {f'admin>menu utama>lihat data>lihat presensi admin>cari ID>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*24}L I H A T   P R E S E N S I   A D M I N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('\r%A, %d %B %Y | %H:%M:%S')}")
                        print(f'\nHasil Pencarian untuk ID "{search_ID}"\n')
                        print(tabulate.tabulate(filtered_df, headers='keys', tablefmt=kolom_fmt, showindex=False))

                        # PILIH JENIS REKAP
                        rekap_choice = input("\nPilih jenis rekapitulasi\n[1] Minggu Ini\n[2] Minggu Lalu\n[3] Bulan Ini\n[4] Bulan Lalu\n[5] Kembali ke menu utama\n\nMasukkan pilihan : ")
                        now = datetime.datetime.now()

                        # MINGGU INI
                        if rekap_choice == '1':
                            rekap_choice_word = "minggu ini"
                            ulangAdmin4 = False
                            start_date = (now - timedelta(days=now.weekday())).strftime('%Y-%m-%d')
                            end_date = (now + timedelta(days=(6 - now.weekday()))).strftime('%Y-%m-%d')
                            total_days = 7
                        # MINGGU LALU
                        elif rekap_choice == '2':
                            rekap_choice_word = "minggu lalu"
                            ulangAdmin4 = False
                            start_date = (now - timedelta(days=(now.weekday() + 7))).strftime('%Y-%m-%d')
                            end_date = (now - timedelta(days=now.weekday() + 1)).strftime('%Y-%m-%d')
                            total_days = 7
                        # BULAN INI
                        elif rekap_choice == '3':
                            rekap_choice_word = "bulan ini"
                            ulangAdmin4 = False
                            start_date = f'{now.year}-{now.month:02d}-01'
                            last_day = calendar.monthrange(now.year, now.month)[1]
                            end_date = f'{now.year}-{now.month:02d}-{last_day}'
                            total_days = last_day
                        # BULAN LALU
                        elif rekap_choice == '4':
                            rekap_choice_word = "bulan lalu"
                            ulangAdmin4 = False
                            last_month = (now.replace(day=1) - timedelta(days=1)).replace(day=1)
                            start_date = f'{last_month.year}-{last_month.month:02d}-01'
                            last_day = calendar.monthrange(last_month.year, last_month.month)[1]
                            end_date = f'{last_month.year}-{last_month.month:02d}-{last_day}'
                            total_days = last_day
                        # MENGEMBALIKAN KE MENU UTAMA
                        elif rekap_choice == '5':
                            input("\nTekan [enter] untuk kembali ke menu utama")
                            main_page_admin()    

                        else:
                            ulangAdmin4 = True
                    
                    # FILTER DF BERDASARKAN TANGGAL
                    filtered_df = filtered_df.loc[(filtered_df['Tanggal'] >= start_date) & (filtered_df['Tanggal'] <= end_date)]

                    # MENGHITUNG STATISTIK KEHADIRAN
                    total_kehadiran_tepat_waktu = len(filtered_df[filtered_df['Kehadiran'].str.upper() == 'HADIR'])
                    total_terlambat = len(filtered_df[filtered_df['Kehadiran'].str.upper() == 'TERLAMBAT'])
                    total_kehadiran = total_kehadiran_tepat_waktu + total_terlambat
                    total_tidak_hadir = len(filtered_df[filtered_df['Kehadiran'].str.upper() == 'TIDAK HADIR'])

                    total_hari_kerja = total_kehadiran + total_tidak_hadir  # Total hari kerja dihitung berdasarkan jumlah data presensi

                    # MENAMPILKAN STATISTIK KEHADIRAN
                    os.system('cls')
                    print(f'++{'='*86}++\n|| {'admin>menu utama>lihat data>lihat rekapitulasi presensi admin>'f"{rekap_choice_word}"'>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{' '*23}R E K A P I T U L A S I   P R E S E N S I{' '*22}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n\nMenampilkan rekapitulasi "{rekap_choice_word.upper()}"\n{start_date} | {end_date}\n\nTOTAL HADIR : {total_kehadiran}')  # UI HASIL REKAPAN
                    print("dengan rincian :")
                    print(f" > Total Hadir Tepat Waktu: {total_kehadiran_tepat_waktu}")
                    print(f" > Total Terlambat: {total_terlambat}")
                    print(f"TOTAL TIDAK HADIR : {total_tidak_hadir}")

                    # Persentase Kehadiran
                    if total_hari_kerja > 0:
                        attendance_percentage = round((total_kehadiran / total_hari_kerja * 100))
                        print(f"\nPERSENTASE KEHADIRAN ({start_date} sampai {end_date}): \n{attendance_percentage}% ({total_kehadiran} dari {total_hari_kerja} hari kerja)")
                        print("\n[Tutup jendela grafik untuk kembali ke menu]")
                        # MENYIAPKAN GRAFIK DENGAN MATHPLOPLIB
                        plt.figure(figsize=(5, 5)) # UKURAN WINDOW
                        labels = ['Hadir Tepat Waktu', 'Terlambat', 'Tidak Hadir']
                        values = [total_kehadiran_tepat_waktu, total_terlambat, total_tidak_hadir]
                        nama_display = filtered_df.iloc[0,2]

                        plt.bar(labels, values, color=['green', 'orange', 'red'])
                        plt.xlabel('Kategori Kehadiran')
                        plt.ylabel('Jumlah')
                        plt.title(f'Grafik Kehadiran {nama_display}')
                        
                        # ROOT TKINTER
                        root = tk.Tk()
                        root.withdraw()  # SEMBUNYIKAN TK

                        # MEMBUAT WINDOW TK UNTUK PATOKAN POSISI WINDOW PLT
                        top = tk.Toplevel(root)

                        # MENGATUR UKURAN DAN POSISI MEMUNCULKAN KANVAS
                        screen_width = root.winfo_screenwidth()
                        screen_height = root.winfo_screenheight()
                        window_width = 450
                        window_height = 400
                        pos_x = screen_width - window_width - 50  # 50 pixel dari kanan
                        pos_y = screen_height - window_height - 100  # 100 pixel dari bawah

                        top.geometry(f'{window_width}x{window_height}+{pos_x}+{pos_y}')
                        top.update_idletasks()

                        # MEMINDAHKAN WINDOW PLT KE POSISI YANG DIINGINKAN
                        fig_manager = plt.get_current_fig_manager()
                        fig_manager.window.wm_geometry(f"{window_width}x{window_height}+{pos_x}+{pos_y}")

                        # EKSEKUSI
                        root.destroy()  # MENUTUP WINDOW TK KARENA HANYA UNTUK POSITIONING
                        plt.show()      # MEMUNCULKAN GRAFIK

                        # KEMBALI KE MENU
                        main_page_admin()
                        
                    else:
                        print("\nTidak ada data kehadiran pada periode yang dipilih.")
                        input("\nTekan [enter] untuk kembali ke Main Menu")

                    main_page_admin()    # MENGEMBALIKAN KE MENU UTAMA

            else:   # HASIL SEARCHING TIDAK DITEMUKAN
                print("\nData yang anda cari tidak ada...")
                input("\nTekan [enter] untuk kembali ke menu utama")

        # FITUR 5.3 SELESAI : UI : COMMENT : DESAIN

        elif menu_choice_5 == '4':    # FITUR 5.4 LIHAT DATA>LIHAT PRESENSI KARYAWAN
            os.system('cls')
            print(f"++{'='*86}++\n|| {f'admin>menu utama>lihat data>lihat presensi karyawan>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*21}L I H A T   P R E S E N S I   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('\r%A, %d %B %Y | %H:%M:%S')}\n")

            # MENAMPILKAN DATA
            df = pd.DataFrame(data_employee, columns=kolom_employee)    # MEMASUKKAN LIST DATA BESAR KE PANDAS

            # ALGORITMA MERGE SORT
            def merge_sort(df, column):
                if len(df) > 1:
                    mid = len(df) // 2
                    left_half = df.iloc[:mid].copy()
                    right_half = df.iloc[mid:].copy()

                    merge_sort(left_half, column)
                    merge_sort(right_half, column)

                    i = j = k = 0

                    while i < len(left_half) and j < len(right_half):
                        if left_half.iloc[i][column] < right_half.iloc[j][column]:
                            df.iloc[k] = left_half.iloc[i]
                            i += 1
                        else:
                            df.iloc[k] = right_half.iloc[j]
                            j += 1
                        k += 1

                    while i < len(left_half):
                        df.iloc[k] = left_half.iloc[i]
                        i += 1
                        k += 1

                    while j < len(right_half):
                        df.iloc[k] = right_half.iloc[j]
                        j += 1
                        k += 1
            # MELAKUKAN SORTING MENGGUNAKAN ALGORITMA MERGE SORT
            merge_sort(df, 'ID')
            # DISPLAY TABEL
            print(tabulate.tabulate(df.iloc[:, :2], headers="keys", tablefmt=kolom_fmt, showindex=False))

            df = pd.DataFrame(data_presensi, columns=kolom_presensi)  # memasukkan data list ke pandas
            df = df.sort_values(by='ID', ascending=True)  # Sortir berdasarkan ID
            # FITUR SEARCH BERDASARKAN ID
            search_ID = input("\nMasukkan ID yang hendak dilihat : ")

            # BINARY SEARCH
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
                menu_presensi_karyawan = input("Menu :\n[1] Lihat Data Presensi\n[2] Lihat Rekapitulasi Presensi\nMasukan opsi : ")

                if menu_presensi_karyawan == '1':       # FITUR 5.4.1 LIHAT DATA>LIHAT PRESENSI KARYAWAN>LIHAT DATA PRESENSI
                    os.system('cls')
                    print(f"++{'='*86}++\n|| {f'admin>menu utama>lihat data>lihat presensi karyawan>cari ID>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*21}L I H A T   P R E S E N S I   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('\r%A, %d %B %Y | %H:%M:%S')}")

                    filtered_df = df.iloc[[index]]  # deklarasi data hasil filter
                    print(f'\nHasil Pencarian untuk ID "{search_ID}"\n')
                    print(tabulate.tabulate(filtered_df, headers='keys', tablefmt=kolom_fmt, showindex=False))

                    # SEARCHING LAGI DENGAN TANGGAL
                    search_date = input("\nMasukkan Tanggal yang hendak dicari [yyyy-mm-dd] : ")

                    if search_date in filtered_df['Tanggal'].values:  # SEARCHING ADA DI DATABASE
                        os.system('cls')
                        print(f"++{'='*86}++\n|| {f'admin>menu utama>lihat data>lihat presensi karyawan>cari ID>cari tanggal>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*21}L I H A T   P R E S E N S I   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('\r%A, %d %B %Y | %H:%M:%S')}\n")

                        filtered_df = filtered_df.loc[filtered_df['Tanggal'].str.contains(search_date)]
                        print(f'\nHasil Pencarian untuk tanggal "{search_date}"\n')
                        print(tabulate.tabulate(filtered_df, headers='keys', tablefmt=kolom_fmt, showindex=False))
                    else:  # HASIL SEARCHING DENGAN TANGGAL TIDAK DITEMUKAN
                        print("\nData yang anda cari tidak ada...")
                    
                    input("\nTekan [enter] untuk kembali ke menu utama")
                
                elif menu_presensi_karyawan == '2':     # FITUR 5.4.2 LIHAT DATA>LIHAT PRESENSI KARYAWAN>LIHAT REKAPITULASI PRESENSI KARYAWAN
                    
                    # FILTER DF BERDASARKAN ID YANG DICARI
                    filtered_df = df.loc[df['ID'] == search_ID]

                    # PILIHAN REKAP
                    ulangAdmin4 = True
                    while ulangAdmin4:
                        os.system('cls')
                        print(f"++{'='*86}++\n|| {f'admin>menu utama>lihat data>lihat presensi karyawan>cari ID>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*21}L I H A T   P R E S E N S I   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('\r%A, %d %B %Y | %H:%M:%S')}")
                        print(f'\nHasil Pencarian untuk ID "{search_ID}"\n')
                        print(tabulate.tabulate(filtered_df, headers='keys', tablefmt=kolom_fmt, showindex=False))

                        # PILIH JENIS REKAP
                        rekap_choice = input("\nPilih jenis rekapitulasi\n[1] Minggu Ini\n[2] Minggu Lalu\n[3] Bulan Ini\n[4] Bulan Lalu\n[5] Kembali ke menu utama\n\nMasukkan pilihan : ")
                        now = datetime.datetime.now()

                        # MINGGU INI
                        if rekap_choice == '1':
                            rekap_choice_word = "minggu ini"
                            ulangAdmin4 = False
                            start_date = (now - timedelta(days=now.weekday())).strftime('%Y-%m-%d')
                            end_date = (now + timedelta(days=(6 - now.weekday()))).strftime('%Y-%m-%d')
                            total_days = 7
                        # MINGGU LALU
                        elif rekap_choice == '2':
                            rekap_choice_word = "minggu lalu"
                            ulangAdmin4 = False
                            start_date = (now - timedelta(days=(now.weekday() + 7))).strftime('%Y-%m-%d')
                            end_date = (now - timedelta(days=now.weekday() + 1)).strftime('%Y-%m-%d')
                            total_days = 7
                        # BULAN INI
                        elif rekap_choice == '3':
                            rekap_choice_word = "bulan ini"
                            ulangAdmin4 = False
                            start_date = f'{now.year}-{now.month:02d}-01'
                            last_day = calendar.monthrange(now.year, now.month)[1]
                            end_date = f'{now.year}-{now.month:02d}-{last_day}'
                            total_days = last_day
                        # BULAN LALU
                        elif rekap_choice == '4':
                            rekap_choice_word = "bulan lalu"
                            ulangAdmin4 = False
                            last_month = (now.replace(day=1) - timedelta(days=1)).replace(day=1)
                            start_date = f'{last_month.year}-{last_month.month:02d}-01'
                            last_day = calendar.monthrange(last_month.year, last_month.month)[1]
                            end_date = f'{last_month.year}-{last_month.month:02d}-{last_day}'
                            total_days = last_day
                        # MENGEMBALIKAN KE MENU UTAMA
                        elif rekap_choice == '5':
                            input("\nTekan [enter] untuk kembali ke menu utama")
                            main_page_admin()    

                        else:
                            ulangAdmin4 = True
                    
                    # FILTER DF BERDASARKAN TANGGAL
                    filtered_df = filtered_df.loc[(filtered_df['Tanggal'] >= start_date) & (filtered_df['Tanggal'] <= end_date)]

                    # MENGHITUNG STATISTIK KEHADIRAN
                    total_kehadiran_tepat_waktu = len(filtered_df[filtered_df['Kehadiran'].str.upper() == 'HADIR'])
                    total_terlambat = len(filtered_df[filtered_df['Kehadiran'].str.upper() == 'TERLAMBAT'])
                    total_kehadiran = total_kehadiran_tepat_waktu + total_terlambat
                    total_tidak_hadir = len(filtered_df[filtered_df['Kehadiran'].str.upper() == 'TIDAK HADIR'])

                    total_hari_kerja = total_kehadiran + total_tidak_hadir  # Total hari kerja dihitung berdasarkan jumlah data presensi

                    # MENAMPILKAN STATISTIK KEHADIRAN
                    os.system('cls')
                    print(f'++{'='*86}++\n|| {'admin>menu utama>lihat data>lihat rekapitulasi presensi karyawan>'f"{rekap_choice_word}"'>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{' '*23}R E K A P I T U L A S I   P R E S E N S I{' '*22}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n\nMenampilkan rekapitulasi "{rekap_choice_word.upper()}"\n{start_date} | {end_date}\n\nTOTAL HADIR : {total_kehadiran}')  # UI HASIL REKAPAN
                    print("dengan rincian :")
                    print(f" > Total Hadir Tepat Waktu: {total_kehadiran_tepat_waktu}")
                    print(f" > Total Terlambat: {total_terlambat}")
                    print(f"TOTAL TIDAK HADIR : {total_tidak_hadir}")

                    # Persentase Kehadiran
                    if total_hari_kerja > 0:
                        attendance_percentage = round((total_kehadiran / total_hari_kerja * 100))
                        print(f"\nPERSENTASE KEHADIRAN ({start_date} sampai {end_date}): \n{attendance_percentage}% ({total_kehadiran} dari {total_hari_kerja} hari kerja)")
                        print("\n[Tutup jendela grafik untuk kembali ke menu]")
                        # MENYIAPKAN GRAFIK DENGAN MATHPLOPLIB
                        plt.figure(figsize=(5, 5)) # UKURAN WINDOW
                        labels = ['Hadir Tepat Waktu', 'Terlambat', 'Tidak Hadir']
                        values = [total_kehadiran_tepat_waktu, total_terlambat, total_tidak_hadir]
                        nama_display = filtered_df.iloc[0,2]
                        plt.bar(labels, values, color=['green', 'orange', 'red'])
                        plt.xlabel('Kategori Kehadiran')
                        plt.ylabel('Jumlah')
                        plt.title(f'Grafik Kehadiran {nama_display}')

                        # ROOT TKINTER
                        root = tk.Tk()
                        root.withdraw()  # SEMBUNYIKAN TK

                        # MEMBUAT WINDOW TK UNTUK PATOKAN POSISI WINDOW PLT
                        top = tk.Toplevel(root)

                        # MENGATUR UKURAN DAN POSISI MEMUNCULKAN KANVAS
                        screen_width = root.winfo_screenwidth()
                        screen_height = root.winfo_screenheight()
                        window_width = 450
                        window_height = 400
                        pos_x = screen_width - window_width - 50  # 50 pixel dari kanan
                        pos_y = screen_height - window_height - 100  # 100 pixel dari bawah

                        top.geometry(f'{window_width}x{window_height}+{pos_x}+{pos_y}')
                        top.update_idletasks()

                        # MEMINDAHKAN WINDOW PLT KE POSISI YANG DIINGINKAN
                        fig_manager = plt.get_current_fig_manager()
                        fig_manager.window.wm_geometry(f"{window_width}x{window_height}+{pos_x}+{pos_y}")

                        # EKSEKUSI
                        root.destroy()  # MENUTUP WINDOW TK KARENA HANYA UNTUK POSITIONING
                        plt.show()      # MEMUNCULKAN GRAFIK

                        # KEMBALI KE MENU
                        main_page_admin()
                        
                    else:
                        print("\nTidak ada data kehadiran pada periode yang dipilih.")
                        input("\nTekan [enter] untuk kembali ke Main Menu")

                    main_page_admin()    # MENGEMBALIKAN KE MENU UTAMA

            else:   # HASIL SEARCHING TIDAK DITEMUKAN
                print("\nData yang anda cari tidak ada...")
                input("\nTekan [enter] untuk kembali ke menu utama")

        # FITUR 5.4 SELESAI : UI : COMMENT : DESAIN

        main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN
    
    # FITUR 5 SELESAI : UI : COMMENT : DESAIN

    elif menu_choice == '6':        # FITUR 6 HAPUS DATA
        menu_choice_6 = input("[1] Hapus Data Admin\n[2] Hapus Data Karyawan\n[3] Hapus Presensi Admin\n[4] Hapus Presensi Karyawan\nPilih menu : ")  # PILIHAN DATA MANA YANG HENDAK DIHAPUS

        if menu_choice_6 == '1':    # FITUR 6.1 HAPUS DATA>HAPUS DATA ADMIN
            os.system('cls')
            print(f"++{'='*86}++\n|| {f"admin>menu utama>hapus data>hapus data admin":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*27}H A P U S   D A T A   A D M I N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n\n\nmenampilkan keseluruhan data...\n") # UI HAPUS DATA
            df = pd.DataFrame(data_admin, columns=kolom_admin)  # MENGUBAH LIST MENJADI TABEL DENGAN PANDAS
            print(tabulate.tabulate(df, headers=kolom_admin, tablefmt=kolom_fmt, showindex=False))    # MENAMPILKAN TABEL KE TERMINAL

            # MENDETEKSI DATA YANG HENDAK DIHAPUS ITU ADA
            menghapus_file = input("\nMasukkan ID admin yang mau dihapus : ")      # user memasukkan data yang ingin dihapus
            # identifikasi data yang akan dihapus didapatkan dari  admin_column = [x[0] for x in data_admin]
            print()
            if menghapus_file in admin_column:  # BILA DATA YANG HENDAK DIHAPUS ITU ADA
                for x in range(0,len(data_admin)):  # mencari di seluruh database admin
                    # BILA DATA YANG DICOCOKKAN SAMA DENGAN YANG DICARI
                    if menghapus_file == data_admin[x][0]:  # DATA COCOK
                        os.system('cls')
                        print(f"++{'='*86}++\n|| {f"admin>menu utama>hapus data>hapus data admin>ID:{data_admin[x][0]}":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*27}H A P U S   D A T A   A D M I N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n") # UI HAPUS DATA
                        print(f'Data admin yang akan dihapus :')
                        print(tabulate.tabulate([data_admin[x]], headers=kolom_admin, tablefmt=kolom_fmt, showindex=False))   # KONFIRMASI DATA YANG HENDAK DIHAPUS
                        pilihan_admin_hapus = input("Anda yakin?\nTekan [1] untuk menghapus\nTekan [2] atau [tombol lain] untuk membatalkan : ")    # KONFIRMASI HENDAK MENGHAPUS ATAU TIDAK
                        # DATA JADI DIHAPUS
                        if pilihan_admin_hapus == '1':
                            df = pd.DataFrame(data_admin, columns=kolom_admin)                  # deklarasi tabel pandas
                            df = df.drop(x)                                                     # menghapus data yang diinginkan
                            np.savetxt('admin_account_database.csv',df,delimiter=',',fmt='% s') # meyimpan kembali data yang tidak dihapus
                            os.system('cls')
                            print(f"++{'='*86}++\n|| {f"admin>menu utama>hapus data>hapus data admin>ID:{data_admin[x][0]}":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*27}H A P U S   D A T A   A D M I N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n") # UI HAPUS DATA
                            print(f"ID terhapus : {menghapus_file}")  # IN-PROGRAM-NOTIFICATION DATA YANG TELAH DIHAPUS
                            print(f"Hasil data : \n{tabulate.tabulate(df, headers="keys", tablefmt=kolom_fmt, showindex=False)}")    # DATA TERSISA
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
        
        # FITUR 6.1 SELESAI : UI : COMMENT : DESAIN

        elif menu_choice_6 == '2':    # FITUR 6.2 HAPUS DATA>HAPUS DATA KARYAWAN
            os.system('cls')
            print(f"++{'='*86}++\n|| {f"admin>menu utama>hapus data>hapus data karyawan>":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*24}H A P U S   D A T A   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n\nmenampilkan keseluruhan data...\n")  # UI HAPUS DATA
            df = pd.DataFrame(data_employee, columns=kolom_employee)    # MENGUBAH LIST MENJADI TABEL DENGAN PANDAS
            print(tabulate.tabulate(df, headers=kolom_employee, tablefmt=kolom_fmt, showindex=False))    # MENAMPILKAN TABEL KE TERMINAL

            # MENDETEKSI DATA YANG HENDAK DIHAPUS ITU ADA
            menghapus_file = input("\nMasukkan ID karyawan yang mau dihapus : ")      # user memasukkan data yang ingin dihapus
            # identifikasi data yang akan dihapus didapatkan dari  employee_column = [x[0] for x in data_employee]

            if menghapus_file in employee_column:   # BILA DATA YANG HENDAK DIHAPUS ITU ADA
                for x in range(0,len(data_employee)):   # mencari di seluruh database admin
                    # BILA DATA YANG DICOCOKKAN SAMA DENGAN YANG DICARI
                    if menghapus_file == data_employee[x][0]:   # DATA COCOK
                        os.system('cls')
                        print(f"++{'='*86}++\n|| {f"admin>menu utama>hapus data>hapus data karyawan>ID:{data_employee[x][0]}":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*24}H A P U S   D A T A   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n")
                        print(f'Data karyawan yang akan dihapus :')# KONFIRMASI DATA YANG HENDAK DIHAPUS
                        print(tabulate.tabulate([data_employee[x]], headers=kolom_employee, tablefmt=kolom_fmt, showindex=False))   # KONFIRMASI DATA 
                        pilihan_employee_hapus = input("Anda yakin?\nTekan [1] untuk menghapus\nTekan [2] atau [tombol lain] untuk membatalkan : ") # KONFIRMASI HENDAK MENGHAPUS ATAU TIDAK
                        # DATA JADI DIHAPUS
                        if pilihan_employee_hapus == '1':
                            df = pd.DataFrame(data_employee, columns=kolom_employee)                # deklarasi tabel pandas
                            df = df.drop(x)                                                         # menghapus data yang diinginkan
                            np.savetxt('employee_account_database.csv',df,delimiter=',',fmt='% s')  # meyimpan kembali data yang tidak dihapus
                            os.system('cls')
                            print(f"++{'='*86}++\n|| {f"admin>menu utama>hapus data>hapus data karyawan>ID:{data_employee[x][0]}":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*24}H A P U S   D A T A   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n")
                            print(f"ID dihapus : {menghapus_file}\n") # IN-PROGRAM-NOTIFICATION DATA YANG TELAH DIHAPUS
                            print(f"Hasil data : \n{tabulate.tabulate(df, headers="keys", tablefmt=kolom_fmt, showindex=False)}")    # DATA TERSISA
                            input("\nTekan [enter] untuk kembali ke menu utama")
                            main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN
                        # DATA TIDAK JADI DIHAPUS
                        else:
                            input("\nMembatalkan ... Tekan [enter] untuk kembali ke menu utama")
                            main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN
                    else:   # DATA TIDAK COCOK
                        input("\nData tidak ada ... Tekan [enter] untuk kembali ke menu utama")
                        main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN

            else:   # BILA DATA YANG HENDAK DIHAPUS TIDAK ADA
                input("\nData tidak ada ... Tekan [enter] untuk kembali ke menu utama")
                main_page_admin()   # MENGEMBALIKAN KE MENU UTAMA ADMIN
        
        # FITUR 6.2 SELESAI : UI : COMMENT : DESAIN
         
        elif menu_choice_6 == '3':    # FITUR 6.3 HAPUS PRESENSI ADMIN
            os.system('cls')
            print(f"++{'='*86}++\n|| {f"admin>menu utama>hapus presensi admin>":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*24}H A P U S   P R E S E N S I   A D M I N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n") # UI HAPUS DATA
            df = pd.DataFrame(data_presensi_admin, columns=kolom_presensi)    # MENGUBAH LIST MENJADI TABEL DENGAN PANDAS
            
            # MENCARI TANGGAL YANG HENDAK DIHAPUS ITU ADA
            masukkan_tanggal_presensi = str(input("Masukkan tanggal yang dicari : "))  # user memasukkan data yang ingin dihapus
            
            os.system('cls')
            print(f"++{'='*86}++\n|| {f"admin>menu utama>hapus presensi admin>tanggal:{masukkan_tanggal_presensi}":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*24}H A P U S   P R E S E N S I   A D M I N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n") # UI HAPUS DATA

            # FILTRASI TANGGAL YANG SESUAI DENGAN YANG DICARI
            filtered_df = df.loc[df['Tanggal'].str.contains(masukkan_tanggal_presensi)]        
            print(tabulate.tabulate(filtered_df, headers="keys", tablefmt=kolom_fmt))    # MENAMPILKAN TABEL TANGGAL YANG SESUAI
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
                    np.savetxt("presensi_database_admin.csv",df,delimiter=',',fmt='% s')  
                    os.system('cls')
                    print(f"++{'='*86}++\n|| {f"admin>menu utama>hapus presensi admin>tanggal:{masukkan_tanggal_presensi}":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*24}H A P U S   P R E S E N S I   A D M I N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n") # UI HAPUS DATA
                    print(f"Data {masukkan_hapus_presensi} berhasil dihapus!")  # IN-PROGRAM-NOTIFICATION DATA YANG TELAH DIHAPUS
                    print(f"Data saat ini :\n\n{tabulate.tabulate(df, headers="keys", tablefmt=kolom_fmt, showindex=False)}")    # DATA TERSISA
                    input("\nTekan [enter] untuk kembali ke Main Menu")
                # DATA TIDAK JADI DIHAPUS
                else:
                    input("\nMembatalkan ... Tekan [enter] untuk kembali ke menu utama")

            else:   # INDEX YANG DIPILIH BUKAN YANG DISORTIR
                print("Kesalahan input, index yang dimasukkan tidak dalam jangkauan sortir, atau data tidak ada")
                input("Tekan [Enter] untuk kembali ke Main Menu")
            
        # FITUR 6.3 SELESAI : UI : COMMENT : DESAIN

        elif menu_choice_6 == '4':    # FITUR 6.4 HAPUS PRESENSI KARYAWAN
            os.system('cls')
            print(f"++{'='*86}++\n|| {f"admin>menu utama>hapus presensi karyawan>":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*21}H A P U S   P R E S E N S I   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n") # UI HAPUS DATA
            df = pd.DataFrame(data_presensi, columns=kolom_presensi)    # MENGUBAH LIST MENJADI TABEL DENGAN PANDAS
            
            # MENCARI TANGGAL YANG HENDAK DIHAPUS ITU ADA
            masukkan_tanggal_presensi = str(input("Masukkan tanggal yang dicari : "))  # user memasukkan data yang ingin dihapus
            
            os.system('cls')
            print(f"++{'='*86}++\n|| {f"admin>menu utama>hapus presensi karyawan>tanggal:{masukkan_tanggal_presensi}":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*21}H A P U S   P R E S E N S I   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n") # UI HAPUS DATA

            # FILTRASI TANGGAL YANG SESUAI DENGAN YANG DICARI
            filtered_df = df.loc[df['Tanggal'].str.contains(masukkan_tanggal_presensi)]        
            print(tabulate.tabulate(filtered_df, headers="keys", tablefmt=kolom_fmt))    # MENAMPILKAN TABEL TANGGAL YANG SESUAI
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
                    os.system('cls')
                    print(f"++{'='*86}++\n|| {f"admin>menu utama>hapus presensi karyawan>tanggal:{masukkan_tanggal_presensi}":<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*21}H A P U S   P R E S E N S I   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n") # UI HAPUS DATA
                    print(f"Data {masukkan_hapus_presensi} berhasil dihapus!")  # IN-PROGRAM-NOTIFICATION DATA YANG TELAH DIHAPUS
                    print(f"Data saat ini :\n\n{tabulate.tabulate(df, headers="keys", tablefmt=kolom_fmt, showindex=False)}")    # DATA TERSISA
                    input("\nTekan [enter] untuk kembali ke Main Menu")
                # DATA TIDAK JADI DIHAPUS
                else:
                    input("\nMembatalkan ... Tekan [enter] untuk kembali ke menu utama")

            else:   # INDEX YANG DIPILIH BUKAN YANG DISORTIR
                print("Kesalahan input, index yang dimasukkan tidak dalam jangkauan sortir, atau data tidak ada")
                input("Tekan [Enter] untuk kembali ke Main Menu")
            
        # FITUR 6.4 SELESAI : UI : COMMENT : DESAIN
        
        main_page_admin()

    # FITUR 6 SELESAI : UI : COMMENT : DESAIN

    elif menu_choice == '7':        # FITUR 7 KARYAWAN TERBAIK ATAU TERBURUK
        os.system('cls')
        print(f"++{'='*86}++\n|| {f'admin>menu utama>lihat data>lihat presensi karyawan>urutkan karyawan>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*21}L I H A T   P R E S E N S I   K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('%A, %d %B %Y | %H:%M:%S')}\n")

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

        # Convert DataFrame to list of dictionaries for sorting
        attendance_list = attendance_summary.to_dict('records')

        # Ask for sorting order
        sort_order = input("\nPilih urutan\n[1] Dari terbaik ke terburuk\n[2] Dari terburuk ke terbaik\nMasukkan pilihan : ")

        def merge_sort(arr, key):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left_half = merge_sort(arr[:mid], key)
            right_half = merge_sort(arr[mid:], key)
            return merge(left_half, right_half, key)

        def merge(left, right, key):
            sorted_arr = []
            while left and right:
                if left[0][key] < right[0][key]:
                    sorted_arr.append(left.pop(0))
                else:
                    sorted_arr.append(right.pop(0))
            sorted_arr.extend(left if left else right)
            return sorted_arr
        
        # divide an conquer
        if sort_order == '1':
            sorted_list = merge_sort(attendance_list, 'Total Kehadiran')[::-1]  # best to worst
        elif sort_order == '2':
            sorted_list = merge_sort(attendance_list, 'Total Kehadiran')  # worst to best
        else:
            print("\nPilihan yang anda berikan tidak ada!")
            input("\nTekan [enter] untuk kembali ke menu utama")
            main_page_admin()

        # Convert back to DataFrame
        sorted_df = pd.DataFrame(sorted_list)

        # Plot the data
        plt.figure(figsize=(6, 5))
        plt.bar(sorted_df['Nama'], sorted_df['Total Kehadiran'], color='blue')
        plt.xlabel('Nama Karyawan')
        plt.ylabel('Total Kehadiran')
        plt.title(f'Total Kehadiran Karyawan dari {"terbaik ke terburuk" if sort_order == "1" else "terburuk ke terbaik"} \nuntuk periode "{rekap_choice_word}"')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # ROOT TKINTER
        root = tk.Tk()
        root.withdraw()  # SEMBUNYIKAN TK
        # MEMBUAT WINDOW TK UNTUK PATOKAN POSISI WINDOW PLT
        top = tk.Toplevel(root)
        # MENGATUR UKURAN DAN POSISI MEMUNCULKAN KANVAS
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        window_width = 550
        window_height = 400
        pos_x = screen_width - window_width - 50  # 50 pixel dari kanan
        pos_y = screen_height - window_height - 100  # 100 pixel dari bawah
        top.geometry(f'{window_width}x{window_height}+{pos_x}+{pos_y}')
        top.update_idletasks()
        # MEMINDAHKAN WINDOW PLT KE POSISI YANG DIINGINKAN
        fig_manager = plt.get_current_fig_manager()
        fig_manager.window.wm_geometry(f"{window_width}x{window_height}+{pos_x}+{pos_y}")
        # EKSEKUSI
        root.destroy()  # MENUTUP WINDOW TK KARENA HANYA 

        # Display the plot
        print("\n[Tutup jendela grafik untuk kembali ke Main Menu]")
        plt.show()

        main_page_admin()    # FITUR 7

    # FITUR 7 SELESAI : UI

    elif menu_choice == '8':        # FTUR 8 LEMBUR
        def baca_data_karyawan():
            data_karyawan = []
            try:
                with open("employee_account_database.csv", "r", newline="") as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        data_karyawan.append([row[0],row[1],row[2],row[3]])
            except KeyError as e:
                print(f"Error: Kolom {e} tidak ditemukan di file CSV.")
            return data_karyawan

        def hitung_durasi_jam(jam_mulai, jam_selesai):
            jam_mulai_h, jam_mulai_m = map(int, jam_mulai.split(':'))
            jam_selesai_h, jam_selesai_m = map(int, jam_selesai.split(':'))

            total_menit_mulai = jam_mulai_h * 60 + jam_mulai_m
            total_menit_selesai = jam_selesai_h * 60 + jam_selesai_m

            durasi_menit = total_menit_selesai - total_menit_mulai

            if durasi_menit > 0:
                return durasi_menit // 60
            else:
                return 0

        def baca_perintah_lembur():
            perintah_lembur = []
            try:
                with open("perintah_lembur.csv", "r", newline="") as csvfile:
                    reader = csv.reader(csvfile)
                    # Cek apakah file CSV kosong
                    if sum(1 for row in reader) <= 1:  # Kurang dari atau sama dengan 1 karena satu baris adalah header
                        print("File perintah_lembur.csv kosong.")
                        return perintah_lembur
                    else:
                        csvfile.seek(0)  # Reset posisi file ke awal setelah iterasi sebelumnya
                        next(reader)     # Lewati baris header
                        for row in reader:
                            perintah_lembur.append([row[0],row[1],row[2],row[3],row[4], row[5],row[6]])
            except FileNotFoundError:
                print("File perintah_lembur.csv tidak ditemukan, memulai dengan data lembur kosong.")
            return perintah_lembur

        def catat_lembur(id_karyawan, tgl, jam_mulai, jam_selesai):
            global perintah_lembur
            # Periksa apakah ID karyawan tersedia
            data_karyawan = baca_data_karyawan()
            karyawan = next((data for data in data_karyawan if data[0] == id_karyawan), None)
            if karyawan is None:
                print(f"Error: Employee dengan ID '{id_karyawan}' tidak ditemukan.")
                return



            hari_seminggu = ["SENIN", "SELASA", "RABU", "KAMIS", "JUMAT", "SABTU", "MINGGU"]
            hari_seminggu_inggris = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
            for nomor_hari in range(0,7):
                if (datetime.datetime.now().strftime("%A").upper() == hari_seminggu_inggris[nomor_hari]): 
                    # Mendapatkan nama hari dari tanggal yang dimasukkan
                    hari = hari_seminggu[nomor_hari]

            durasi_jam = hitung_durasi_jam(jam_mulai, jam_selesai)
            perintah_lembur.append([tgl,hari,id_karyawan,karyawan[1],jam_mulai,jam_selesai,durasi_jam])
            print(f"\nLembur untuk ID '{id_karyawan}' pada tanggal {tgl} ({hari}) berhasil dicatat!")

        def buat_csv_lembur():

            with open("perintah_lembur.csv", "w", newline="") as csvfile:
                fieldname = ["tgl", "hari", "id", "nama", "jam_mulai", "jam_selesai", "durasi_jam"]
                writer = csv.writer(csvfile)
                writer.writerow(fieldname)
                for data in perintah_lembur:
                    writer.writerow(data)
            print("Data lembur telah disimpan ke file perintah_lembur.csv")

        def lihat_perintah_lembur():
            global perintah_lembur
            if perintah_lembur:
                while True:
                    print("Pilih Rentang Waktu:")
                    print("[1] Hari Ini")
                    print("[2] Minggu Ini")
                    print("[3] Bulan Ini")
                    print("[4] Semua")
                    print("[5] Kembali ke Menu Utama")
                    
                    rentang_waktu = input("Pilih rentang waktu: ")
                    
                    if rentang_waktu == "1":
                        rentang_waktu_str = "hari ini"
                    elif rentang_waktu == "2":
                        rentang_waktu_str = "minggu ini"
                    elif rentang_waktu == "3":
                        rentang_waktu_str = "bulan ini"
                    elif rentang_waktu == "4":
                        rentang_waktu_str = "semua"
                    elif rentang_waktu == "5":
                        return  # Kembali ke menu utama
                    else:
                        print("Pilihan tidak valid, silakan coba lagi.")
                        continue

                    data = []
                    hari_ini = datetime.datetime.now().date()
                    if rentang_waktu_str == "hari ini":
                        for entry in perintah_lembur:
                            if entry[0] == str(hari_ini):
                                data.append([entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6]])
                    elif rentang_waktu_str == "minggu ini":
                        minggu_ini = hari_ini - timedelta(days=hari_ini.weekday())
                        for entry in perintah_lembur:
                            entry_date = datetime.datetime.strptime(entry[0], "%Y-%m-%d").date()
                            if minggu_ini <= entry_date <= hari_ini:
                                data.append([entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6]])
                    elif rentang_waktu_str == "bulan ini":
                        bulan_ini = hari_ini.replace(day=1)
                        for entry in perintah_lembur:
                            entry_date = datetime.datetime.strptime(entry[0], "%Y-%m-%d").date()
                            if entry_date.month == bulan_ini.month:
                                data.append([entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6]])
                    else:  # Semua data
                        for entry in perintah_lembur:
                            print(entry)
                            data.append([entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6]])

                    headers = ["Tanggal", "Hari", "ID", "Nama", "Jam Mulai", "Jam Selesai", "Durasi Jam"]
                    os.system('cls')
                    print(f"++{'='*86}++\n|| {f'admin>menu utama>lembur>lihat data lembur>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*35}L E M B U R':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('%A, %d %B %Y | %H:%M:%S')}\n")
                    print(tabulate.tabulate(data, headers=headers, tablefmt=kolom_fmt))
                    
                    input("Tekan enter untuk kembali ke menu")
                    break
            else:
                print("Tidak ada data lembur yang tersedia.")

        def hapus_lembur():
            global perintah_lembur
            if not perintah_lembur:
                print("Tidak ada data lembur untuk dihapus.")
                return

            print("Data Lembur:")
            
            perintah_lembur = pd.DataFrame(perintah_lembur)

            header = ['tgl','hari','id','nama','jam_mulai','jam_selesai','durasi_jam']
            print(tabulate.tabulate(perintah_lembur, headers=header, tablefmt=kolom_fmt,))
            try:
                pilihan_hapus = int(input("Pilih nomor lembur yang ingin dihapus: "))
                if 0 <= pilihan_hapus < len(perintah_lembur):
                    perintah_lembur.drop(index=pilihan_hapus, inplace=True)
                    print("Data lembur berhasil dihapus.")
                    perintah_lembur = perintah_lembur.values.tolist()
                    buat_csv_lembur()
                else:
                    print("Pilihan tidak valid.")
            except Exception as e:
                print("PERHATIAN : Pilihan anda tidak valid")
            finally:
                def is_df(var):
                    return isinstance(var, pd.DataFrame)
                if is_df(perintah_lembur):
                    perintah_lembur = perintah_lembur.values.tolist()

        def menu():
            global perintah_lembur
            perintah_lembur = baca_perintah_lembur()
            while True:
                os.system('cls')
                print(f"++{'='*86}++\n|| {f'admin>menu utama>lembur>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*35}L E M B U R':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('%A, %d %B %Y | %H:%M:%S')}\n")

                print("[1] Perintahkan Lembur")
                print("[2] Lihat Semua Data Lembur")
                print("[3] Hapus Lembur")
                print("[4] Keluar")
                
                pilihan = input("Pilih opsi : ")
                
                if pilihan == "1":
                    os.system('cls')
                    print(f"++{'='*86}++\n|| {f'admin>menu utama>lembur>perintahkan lembur>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*35}L E M B U R':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('%A, %d %B %Y | %H:%M:%S')}\n")

                    id_karyawan = input("Masukkan ID karyawan: ")
                    tgl = input("Masukkan tanggal (YYYY-MM-DD): ")
                    jam_mulai = input("Masukkan jam mulai (HH:MM): ")
                    jam_selesai = input("Masukkan jam selesai (HH:MM): ")
                    catat_lembur(id_karyawan, tgl, jam_mulai, jam_selesai)
                    buat_csv_lembur()
                    input("\nTekan [Enter] untuk kembali ke menu")
                elif pilihan == "2":
                    os.system('cls')
                    print(f"++{'='*86}++\n|| {f'admin>menu utama>lembur>lihat data lembur>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*35}L E M B U R':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('%A, %d %B %Y | %H:%M:%S')}\n")
                    lihat_perintah_lembur()
                elif pilihan == "3":
                    os.system('cls')
                    print(f"++{'='*86}++\n|| {f'admin>menu utama>lembur>hapus lembur>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*35}L E M B U R':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('%A, %d %B %Y | %H:%M:%S')}\n")
                    hapus_lembur()
                    input("Tekan [Enter] untuk kembali ke menu")
                elif pilihan == "4":
                    main_page_admin()
                else:
                    menu()

        menu()

    # FITUR 8 SELESAI : UI 

    elif menu_choice == '9':        # FITUR 9 PENGGAJIAN
        def penggajian():
            os.system('cls')
            print(f"++{'='*86}++\n|| {f'admin>menu utama>penggajian>':<85}||\n++{'-'*86}++\n||{' '*86}||\n||{f'{' '*21}P E N G G A J I A N  K A R Y A W A N':<86}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('%A, %d %B %Y | %H:%M:%S')}\n")

            # Membaca file csv dari ketiga csv
            try:
                kolom_employee = ['ID', 'Nama', 'Posisi', 'Password']
                kolom_lembur = ["Tanggal", "Hari", "ID", "Nama", "Jam Mulai", "Jam Selesai", "durasi_jam"]
                kolom_presensi = ["Tanggal", "ID", "Nama", "Hari Kerja", "Kehadiran", "Waktu"]
                employee_df = pd.read_csv('employee_account_database.csv', names=kolom_employee, header=None)
                lembur_df = pd.read_csv('perintah_lembur.csv', names=kolom_lembur, header=None)
                presensi_df = pd.read_csv('presensi_database.csv', names=kolom_presensi, header=None)
            except FileNotFoundError as e:
                print(f"Error: {e}")
                input("Tekan [enter] untuk kembali ke menu utama")
                return

            # Set ongkos lembur per jam dan potongan per jam keterlambatan dan per hari ketidakhadiran
            ongkos_lembur_per_jam = 50000
            potongan_per_jam_telat = 10000
            potongan_per_hari_absen = 100000

            # Daftar posisi karyawan
            posisi_karyawan = [
                'Sekretaris', 'Akuntan', 'Sales Representative', 'Tax', 'CS', 'Admin',
                'HR', 'Digital Marketing', 'Designer', 'PM', 'Developer', 'Data Analyst'
            ]

            # Menampilkan menu pilihan posisi
            print("Pilih posisi karyawan:")
            for i, posisi in enumerate(posisi_karyawan, 1):
                print(f"{i}. {posisi}")

            # Input pilihan posisi
            while True:
                try:
                    pilihan = int(input("Masukkan nomor posisi yang dipilih: "))
                    if 1 <= pilihan <= len(posisi_karyawan):
                        posisi_terpilih = posisi_karyawan[pilihan - 1].upper()  # Konversi ke huruf besar
                        karyawan_terpilih = employee_df[employee_df['Posisi'].str.upper() == posisi_terpilih]  # Bandingkan dalam huruf besar
                        print(f"\nPosisi yang dipilih: {posisi_terpilih.title()}\n")

                        if karyawan_terpilih.empty:
                            input(f"Tidak ada karyawan untuk posisi: {posisi_terpilih.title()}. Tekan [enter] untuk keluar.")
                            return
                        else:
                            break
                    else:
                        input("Nomor posisi tidak valid. Silakan coba lagi. Tekan [enter] untuk melanjutkan.")
                except ValueError as e:
                    input(f"{e}. Input tidak valid. Silakan masukkan nomor posisi. Tekan [enter] untuk melanjutkan.")

            # Tentukan gaji pokok berdasarkan posisi karyawan
            gaji_pokok_map = {
                'SEKRETARIS': 4000000,
                'AKUNTAN': 6000000,
                'SALES REPRESENTATIVE': 5000000,
                'TAX': 6000000,
                'CS': 3500000,
                'ADMIN': 4000000,
                'HR': 4500000,
                'DIGITAL MARKETING': 5500000,
                'DESIGNER': 5000000,
                'PM': 7000000,
                'DEVELOPER': 8000000,
                'DATA ANALYST': 6000000
            }

            # Pastikan kolom 'durasi_jam' ada dan berisi nilai float
            if 'durasi_jam' in lembur_df.columns:
                lembur_df['durasi_jam'] = pd.to_numeric(lembur_df['durasi_jam'], errors='coerce').fillna(0).astype(float)
                total_lembur = lembur_df.groupby('ID')['durasi_jam'].sum().reset_index()
                total_lembur['Ongkos_Lembur'] = total_lembur['durasi_jam'] * ongkos_lembur_per_jam
            else:
                print("Kolom 'durasi_jam' tidak ditemukan dalam DataFrame lembur. Pastikan kolom tersebut ada di file CSV.")
                input("Tekan [enter] untuk kembali ke menu utama")
                return

            # Hitung total keterlambatan
            presensi_df['Waktu'] = pd.to_datetime(presensi_df['Waktu'], errors='coerce').dt.time

            presensi_df['TERLAMBAT'] = presensi_df.apply(
                lambda row: max(
                    (datetime.datetime.combine(datetime.date.today(), row['Waktu']) - datetime.datetime.combine(datetime.date.today(), datetime.time(9, 0))).seconds // 3600, 0
                ) if row['Kehadiran'] == 'HADIR' and row['Waktu'] > datetime.time(9, 0) else 0, axis=1
            )
            total_telat = presensi_df.groupby('ID')['TERLAMBAT'].sum().reset_index()
            total_telat['Potongan_Telat'] = total_telat['TERLAMBAT'] * potongan_per_jam_telat

            # Hitung total ketidakhadiran
            absensi_df = presensi_df[(presensi_df['Kehadiran'] == 'TIDAK HADIR') & (presensi_df['Hari Kerja'] == 'Ya')]
            total_absen = absensi_df.groupby('ID').size().reset_index(name='Total_Tidak_Hadir')
            total_absen['Potongan_Absensi'] = total_absen['Total_Tidak_Hadir'] * potongan_per_hari_absen

            # Merge data untuk penggajian
            penggajian_df = pd.merge(karyawan_terpilih, total_lembur, on='ID', how='left').fillna(0)
            penggajian_df = pd.merge(penggajian_df, total_telat[['ID', 'Potongan_Telat']], on='ID', how='left').fillna(0)
            penggajian_df = pd.merge(penggajian_df, total_absen[['ID', 'Potongan_Absensi']], on='ID', how='left').fillna(0)

            # Tentukan gaji pokok berdasarkan posisi karyawan
            penggajian_df['Gaji_Pokok'] = penggajian_df['Posisi'].map(gaji_pokok_map)

            # Hitung Gaji Bersih
            penggajian_df['Gaji_Bersih'] = penggajian_df['Gaji_Pokok'] + penggajian_df['Ongkos_Lembur'] - penggajian_df['Potongan_Telat'] - penggajian_df['Potongan_Absensi']

            # Kolom yang ingin disimpan
            kolom_penggajian = ['ID', 'Nama', 'Posisi', 'Gaji_Pokok', 'Ongkos_Lembur', 'Potongan_Telat', 'Potongan_Absensi', 'Gaji_Bersih']

            # Save the DataFrame to CSV
            with open('employee_penggajian.csv', mode='a', newline='') as file:
                penggajian_df.to_csv(file, index=False, header=file.tell() == 0)

            # Print the DataFrame using tabulate with formatted values
            penggajian_df[kolom_penggajian] = penggajian_df[kolom_penggajian].applymap(lambda x: f"{x:,.0f}" if isinstance(x, (int, float)) else x)
            print("\nHasil Penggajian Karyawan:")
            print(tabulate.tabulate(penggajian_df[kolom_penggajian], headers='keys', tablefmt='fancy_grid'))

            input("\nTekan [enter] untuk kembali ke menu utama")
            main_page_admin()

        penggajian()

    # FITUR 9 

    elif menu_choice == '10':    # kembali ke launch page
        launchPage()

    # FITUR 10 SELESAI - UI : COMMENT : DESAIN

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
    
    # MENGIMPOR DATA PERINTAH LEMBUR
    data_perintah_lembur = []  # VARIABEL KOSONG UNTUK MENYIMPAN DATA PERINTAH LEMBUR
    with open('perintah_lembur.csv') as csvfile_perintah_lembur:     # MEMBUKA .CSV PERINTAH
        reader_perintah_lembur = csv.reader(csvfile_perintah_lembur)      # menjadikan file .csv menjadi list perintah (menambahkan tiap baris pada .csv kedalam variabel data perintah)
        for row in reader_perintah_lembur:
            data_perintah_lembur.append(row)

    # MENGIMPOR DATA PRESENSI LEMBUR
    data_presensi_lembur = []  # VARIABEL KOSONG UNTUK MENYIMPAN DATA PRESENSI LEMBUR
    with open('employee_presensi_lembur.csv') as csvfile_presensi_lembur:     # MEMBUKA .CSV PRESENSI
        reader_presensi_lembur = csv.reader(csvfile_presensi_lembur)      # menjadikan file .csv menjadi list presensi (menambahkan tiap baris pada .csv kedalam variabel data presensi)
        for row in reader_presensi_lembur:
            data_presensi_lembur.append(row)

    # MEMBUAT DATA PENGKONDISIAN UNTUK PENGECEKAN DATA SUDAH ADA ATAU BELUM
    data_presensi_cond = [] # VARIABEL KOSONG UNTUK MENYIMPAN DATA KONDISI
    g=0 # TRIGGER BARIS KE-
    with open('presensi_database.csv') as csvfile_presensi:     # MEMBUKA .CSV PRESENSI
        reader_presensi = csv.reader(csvfile_presensi)      #menjadikan file .csv menjadi list presensi (menambahkan tiap baris pada .csv kedalam variabel data presensi)
        for row in reader_presensi:
            data_presensi_cond.append(row)
            data_presensi_cond[g][-1] = ""      # MENAMBAHKAN TIAP DATA PRESENSI KE VARIABEL KONDISI DENGAN MENGHAPUS DATA KOLOM "WAKTU"
            g+=1

    # MENDETEKSI NAMA MENGGUNAKAN ID
    if launch_ID in employee_column:    # ID DAN PASSCODE ADA DI DATABASE
        for x in range(0,len(data_employee)):       # mencocokkan ID hasil login dengan ID di database
            if launch_ID == data_employee[x][0]:    # ID DAN PASSCODE SESUAI DENGAN DATABASE ADMIN
                global tujuan   # index orang yang dituju saat menggunakan semua menu karyawan
                tujuan = x
                print(f'Selamat Datang, karyawan "{data_employee[x][1]}"! Apa yang ingin anda lakukan saat ini?\n') # selamat datang karyawan

    print('\nMenu:\n[1] PRESENSI SEKARANG!\n[2] Lihat Jadwal Kerja Anda\n[3] Lihat Rekapitulasi Presensi\n[4] Lihat Data Presensi Anda\n[5] LEMBUR\n[6] Gaji Anda\n[7] Informasi Mengenai Program\n[8] Keluar') # pilihan menu karyawan
    menu_choice = input("Pilih menu : ")
    print()

    if menu_choice == '1':          # FITUR 1 PRESENSI SEKARANG
        # UI PRESENSI SEKARANG DAN PILIHAN SHIFT
        os.system('cls')
        print(f'++{'='*86}++\n|| admin>menu utama>presensi sekarang!>{' '*46}||\n++{'-'*86}++\n||{' '*86}||\n||{' '*26}P R E S E N S I   S E K A R A N G !{' '*25}||\n||{' '*86}||\n++{'='*86}++\nwaktu : {datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n\n')  

        tanggal_presensi = datetime.datetime.now().strftime("%Y-%m-%d") # indikator tanggal riil

        hari_seminggu = ["SENIN", "SELASA", "RABU", "KAMIS", "JUMAT", "SABTU", "MINGGU"]
        for nomor_hari in range(3,10):
    
            # KARYAWAN YANG HENDAK PRESENSI BENAR DI SENIN-JUMAT
            if datetime.datetime.now().strftime("%A").upper() != "SATURDAY" and datetime.datetime.now().strftime("%A").upper() != "SUNDAY":  
    
                time_range = DateTimeRange(open_presensi,close_presensi)
                x = datetime.datetime.now().strftime("%H:%M:%S")    # DEKLARASI WAKTU TERBARU
                
                # BILA DALAM WAKTU GLOBAL PRESENSI
                if x in DateTimeRange(open_presensi,global_close_presensi):   # ABSENSI GLOBAL DIBUKA
                    # DALAM RENTANG PRESENSI
                    if x in time_range :    
                        status_kehadiran = "HADIR" 
                    # TIDAK DALAM RENTANG PRESENSI TAPI MASIH PADA SHIFT
                    elif x in time_range_kerja:    
                        status_kehadiran = "TERLAMBAT"
                    # PRESENSI DILUAR JAM SHIFT
                    else :          
                        input("\nPERHATIAN : Bukan jadwal presensi! Tekan [enter] untuk kembali ke menu utama")
                        status_kehadiran = "TIDAK HADIR"
                        main_page_employee()    # MENGEMBALIKAN KE MENU UTAMA
                    
                    # MEMBUAT DATA UNTUK DIMASUKKAN
                    data_baru = [tanggal_presensi, data_employee[tujuan][0], data_employee[tujuan][1], hari_seminggu[nomor_hari], status_kehadiran, now_time.strftime("%H:%M:%S")]
                    # MEMBUAT DATA PENGKONDISIAN UNTUK MENGECEK DATA SUDAH ADA ATAU BELUM
                    data_baru_cond = [f'{tanggal_presensi}', f'{data_employee[tujuan][0]}', f'{data_employee[tujuan][1]}', f'{hari_seminggu[nomor_hari]}', f'{status_kehadiran}', '']
                    
                    # MENDETEKSI APAKAH KARYAWAN SUDAH MELAKUKAN PRESENSI DI SHIFT YANG SAMA HARI INI
                    # KARYAWAN BELUM PRESENSI
                    if data_baru_cond not in data_presensi_cond:    
                        data_presensi.append(data_baru) # Menambahkan data baru ke dalam list data_presensi
                        with open('presensi_database.csv', 'w', newline='') as csvfile_presensi:    # Membuka file CSV dalam mode penulisan dan menulis data baru ke dalamnya
                            writer_presensi = csv.writer(csvfile_presensi)
                            writer_presensi.writerows(data_presensi)
                        # IN-PROGRAM-NOTIFICATION DATA DICATAT
                        input(f'\nPresensi : {tanggal_presensi},{now_time.strftime("%H:%M:%S")},{data_employee[tujuan][0]},{data_employee[tujuan][1]},{hari_seminggu[nomor_hari]},{status_kehadiran} \nPERHATIAN : Presensi berhasil direkam!\n\nTekan [enter] untuk kembali ke menu utama')   
                    # KARYAWAN SUDAH PRESENSI SEBELUMNYA
                    # IN-PROGRAM-NOTIFICATION DATA SUDAH ADA
                    else:
                        input(f'\nPERHATIAN : Data presensi "{tanggal_presensi},{data_employee[tujuan][0]},{data_employee[tujuan][1]},{hari_seminggu[nomor_hari]},{status_kehadiran}" sudah ada!\n\nTekan [enter] untuk kembali ke menu utama')    
                
                # ABSENSI GLOBAL BELUM DIBUKA
                elif x in pre_presensi:     
                    # MENGEMBALIKAN KE MENU UTAMA
                    input("\nPERHATIAN : Waktu belum menunjukkan jadwal presensi!\n\nTekan [enter] untuk kembali ke menu utama")
            
            # KARYAWAN YANG HENDAK PRESENSI BUKAN MERUPAKAN KARYAWAN SHIFT TERSEBUT
            else:   
                input("\nPERHATIAN : Bukan jadwal presensi anda! Tekan [enter] untuk melanjutkan")
            main_page_employee()

    # FITUR 1 SELESAI - UI : COMMENT : DESAIN

    elif menu_choice == '2':  # FITUR 2 LIHAT JADWAL KERJA
        os.system('cls')  # Membersihkan layar konsol
        print(f"++{'='*86}++\n|| karyawan>menu utama>lihat jadwal kerja>{' '*46}||\n++{'-'*86}++\n||{' '*86}||\n||{' '*21}L I H A T   J A D W A L  K E R J A  A N D A{' '*21}||\n||{' '*86}||\n++{'='*86}++\n{datetime.datetime.now().strftime('%A, %d %B %Y | %H:%M:%S')}\n")    # UI LIHAT JADWAL Kerja
        waktu_kerja = """           
        08:00:00 - 08:59:59 waktu presensi
        09:00:00 - 17:00:00 jam kerja 
        """
        print(waktu_kerja)# UI LIHAT JADWAL Kerja
        input("\n\n\nTekan [enter] untuk kembali ke Main Menu")
        main_page_employee()    # MENGEMBALIKAN KE MENU UTAMA

    # FITUR 2 SELESAI

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

    # FITUR 3 SELESAI

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

    # FITUR 4 SELESAI

    elif menu_choice == '5':  # FITUR 5 LEMBUR
        def presensi_sekarang_lembur():
            # UI PRESENSI SEKARANG DAN PILIHAN SHIFT
            os.system('cls')
            print(f'++{'='*86}++\n|| karyawan>menu utama>lembur>presensi sekarang!>{' '*46}||\n++{'-'*86}++\n||{' '*86}||\n||{' '*26}P R E S E N S I   S E K A R A N G !{' '*25}||\n||{' '*86}||\n++{'='*86}++\nwaktu : {datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n\n')  

            tanggal_presensi = datetime.datetime.now().strftime("%Y-%m-%d") # indikator tanggal riil

            hari_seminggu = ["SENIN", "SELASA", "RABU", "KAMIS", "JUMAT", "SABTU", "MINGGU"]
            for nomor_hari in range(3,10):
        
                # KARYAWAN YANG HENDAK PRESENSI BENAR DI SENIN-JUMAT
                if datetime.datetime.now().strftime("%A").upper() != "SATURDAY" and datetime.datetime.now().strftime("%A").upper() != "SUNDAY":  
        
                    time_range = DateTimeRange(open_presensi,close_presensi)
                    x = datetime.datetime.now().strftime("%H:%M:%S")    # DEKLARASI WAKTU TERBARU
                    
                    # BILA DALAM WAKTU GLOBAL PRESENSI
                    if x in DateTimeRange(open_presensi,global_close_presensi):   # ABSENSI GLOBAL DIBUKA
                        # DALAM RENTANG PRESENSI
                        if x in time_range :    
                            status_kehadiran = "HADIR" 
                        # TIDAK DALAM RENTANG PRESENSI TAPI MASIH PADA SHIFT
                        elif x in time_range_kerja:    
                            status_kehadiran = "TERLAMBAT"
                        # PRESENSI DILUAR JAM SHIFT
                        else :          
                            input("\nPERHATIAN : Bukan jadwal presensi! Tekan [enter] untuk kembali ke menu utama")
                            status_kehadiran = "TIDAK HADIR"
                            main_page_employee()    # MENGEMBALIKAN KE MENU UTAMA
                        
                        # MEMBUAT DATA UNTUK DIMASUKKAN
                        data_baru = [tanggal_presensi, data_employee[tujuan][0], data_employee[tujuan][1], hari_seminggu[nomor_hari], status_kehadiran, now_time.strftime("%H:%M:%S")]
                        # MEMBUAT DATA PENGKONDISIAN UNTUK MENGECEK DATA SUDAH ADA ATAU BELUM
                        data_baru_cond = [f'{tanggal_presensi}', f'{data_employee[tujuan][0]}', f'{data_employee[tujuan][1]}', f'{hari_seminggu[nomor_hari]}', f'{status_kehadiran}', '']
                        
                        # MENDETEKSI APAKAH KARYAWAN SUDAH MELAKUKAN PRESENSI DI SHIFT YANG SAMA HARI INI
                        # KARYAWAN BELUM PRESENSI
                        if data_baru_cond not in data_presensi_cond:    
                            data_presensi.append(data_baru) # Menambahkan data baru ke dalam list data_presensi
                            with open('employee_presensi_lembur.csv', 'w', newline='') as csvfile_presensi:    # Membuka file CSV dalam mode penulisan dan menulis data baru ke dalamnya
                                writer_presensi = csv.writer(csvfile_presensi)
                                writer_presensi.writerows(data_presensi)
                            # IN-PROGRAM-NOTIFICATION DATA DICATAT
                            input(f'\nPresensi : {tanggal_presensi},{now_time.strftime("%H:%M:%S")},{data_employee[tujuan][0]},{data_employee[tujuan][1]},{hari_seminggu[nomor_hari]},{status_kehadiran} \nPERHATIAN : Presensi berhasil direkam!\n\nTekan [enter] untuk kembali ke menu utama')   
                        # KARYAWAN SUDAH PRESENSI SEBELUMNYA
                        # IN-PROGRAM-NOTIFICATION DATA SUDAH ADA
                        else:
                            input(f'\nPERHATIAN : Data presensi "{tanggal_presensi},{data_employee[tujuan][0]},{data_employee[tujuan][1]},{hari_seminggu[nomor_hari]},{status_kehadiran}" sudah ada!\n\nTekan [enter] untuk kembali ke menu utama')    
                    
                    # ABSENSI GLOBAL BELUM DIBUKA
                    elif x in pre_presensi:     
                        # MENGEMBALIKAN KE MENU UTAMA
                        input("\nPERHATIAN : Waktu belum menunjukkan jadwal presensi!\n\nTekan [enter] untuk kembali ke menu utama")
                
                # KARYAWAN YANG HENDAK PRESENSI BUKAN MERUPAKAN KARYAWAN SHIFT TERSEBUT
                else:   
                    input("\nPERHATIAN : Bukan jadwal presensi anda! Tekan [enter] untuk melanjutkan")
                    
                menu_lembur_karyawan()
        
        def lihat_riwayat_lembur():
            perintah_lembur = []
            try:
                with open("perintah_lembur.csv", "r", newline="") as csvfile:
                    reader = csv.DictReader(csvfile, fieldnames=["tgl", "hari", "id", "nama", "jam_mulai", "jam_selesai", "durasi_jam"])
                    # Cek apakah file CSV kosong
                    if sum(1 for row in reader) <= 1:  # Kurang dari atau sama dengan 1 karena satu baris adalah header
                        print("File perintah_lembur.csv kosong.")
                        
                    else:
                        csvfile.seek(0)  # Reset posisi file ke awal setelah iterasi sebelumnya
                        next(reader)     # Lewati baris header
                        for row in reader:
                            perintah_lembur.append({
                                "tgl": row["tgl"],
                                "hari": row["hari"],
                                "id": row["id"],
                                "nama": row["nama"],
                                "jam_mulai": row["jam_mulai"],
                                "jam_selesai": row["jam_selesai"],
                                "durasi_jam": row["durasi_jam"]
                            })
                        
            except FileNotFoundError:
                print("File perintah_lembur.csv tidak ditemukan, memulai dengan data lembur kosong.")
            
            if perintah_lembur:
                while True:
                    os.system('cls')
                    print("\nPilih Rentang Waktu:")
                    print("1. Hari Ini")
                    print("2. Minggu Ini")
                    print("3. Bulan Ini")
                    print("4. Semua")
                    print("5. Kembali ke Menu Utama")
                    
                    rentang_waktu = input("Pilih rentang waktu: ")
                    
                    if rentang_waktu == "1":
                        rentang_waktu_str = "hari ini"
                    elif rentang_waktu == "2":
                        rentang_waktu_str = "minggu ini"
                    elif rentang_waktu == "3":
                        rentang_waktu_str = "bulan ini"
                    elif rentang_waktu == "4":
                        rentang_waktu_str = "semua"
                    elif rentang_waktu == "5":
                        return  # Kembali ke menu utama
                    else:
                        print("Pilihan tidak valid, silakan coba lagi.")
                        continue

                    data = []
                    hari_ini = datetime.datetime.now().date()
                    if rentang_waktu_str == "hari ini":
                        for entry in perintah_lembur:
                            if entry['tgl'] == str(hari_ini):
                                data.append([entry['tgl'], entry['hari'], entry['id'], entry['nama'], entry['jam_mulai'], entry['jam_selesai'], entry['durasi_jam']])
                    elif rentang_waktu_str == "minggu ini":
                        minggu_ini = hari_ini - timedelta(days=hari_ini.weekday())
                        for entry in perintah_lembur:
                            entry_date = datetime.datetime.strptime(entry['tgl'], "%Y-%m-%d").date()
                            if minggu_ini <= entry_date <= hari_ini:
                                data.append([entry['tgl'], entry['hari'], entry['id'], entry['nama'], entry['jam_mulai'], entry['jam_selesai'], entry['durasi_jam']])
                    elif rentang_waktu_str == "bulan ini":
                        bulan_ini = hari_ini.replace(day=1)
                        for entry in perintah_lembur:
                            entry_date = datetime.datetime.strptime(entry['tgl'], "%Y-%m-%d").date()
                            if entry_date.month == bulan_ini.month:
                                data.append([entry['tgl'], entry['hari'], entry['id'], entry['nama'], entry['jam_mulai'], entry['jam_selesai'], entry['durasi_jam']])
                    else:  # Semua data
                        for entry in perintah_lembur:
                            data.append([entry['tgl'], entry['hari'], entry['id'], entry['nama'], entry['jam_mulai'], entry['jam_selesai'], entry['durasi_jam']])

                    headers = ["Tanggal", "Hari", "ID", "Nama", "Jam Mulai", "Jam Selesai", "Durasi Jam"]
                    print(tabulate.tabulate(data, headers=headers, tablefmt="grid"))
                    
                    input("Tekan enter untuk kembali ke menu")
                    
            else:
                print("Tidak ada data lembur yang tersedia.")
            menu_lembur_karyawan()

        def menu_lembur_karyawan():
            os.system('cls')
            print(f'++{'='*86}++\n|| karyawan>menu utama>lembur>{' '*58}||\n++{'-'*86}++\n||{' '*86}||\n||{' '*26}            L E M B U R            {' '*25}||\n||{' '*86}||\n++{'='*86}++\nwaktu : {datetime.datetime.now().strftime("\r%A, %d %B %Y | %H:%M:%S")}\n\n')  
            print("\nMenu LEMBUR :")
            print("[1] PRESENSI LEMBUR SEKARANG!")
            print("[2] Lihat riwayat lembur")
            print("\n[3] Kembali ke Menu Utama")
            menu_choice_5 = input("Pilih menu : ")
            
            if menu_choice_5 == '1':    # FITUR 5.1 PRESENSI SEKARANG
                presensi_sekarang_lembur()
            
            # FITUR 5.1 SELESAI - UI : COMMENT : DESAIN

            elif menu_choice_5 == '2':  # FITUR 5.2 LIHAT RIWAYAT LEMBUR
                lihat_riwayat_lembur()
            
            # FITUR 5.2

            elif menu_choice_5 == '3':  # FITUR 5.3 EXIT
                main_page_employee()
            
            # FITUR 5.3 SELESAI - UI : COMMENT : DESAIN

            menu_lembur_karyawan()

        menu_lembur_karyawan()

    # FITUR 5 tinggal r nya brili

    elif menu_choice == '6':  # FITUR 6 GAJI ANDA
        def cetak_slip(launch_ID):
            os.system('cls')  # Bersihkan console
            print(f'++{"="*86}++\n|| karyawan>menu utama>gaji anda>{" "*46}||\n++{"-"*86}++\n||{" "*86}||\n||{" "*26}S L I P  G A J I  A N D A{" "*25}||\n||{" "*86}||\n++{"="*86}++\nwaktu : {datetime.datetime.now().strftime("%A, %d %B %Y | %H:%M:%S")}\n\n')
           
            with open('employee_penggajian.csv', 'r') as penggajian_file:
                data_penggajian = penggajian_file.readlines()


            # Asumsi nama kolom file CSV adalah seperti berikut
            kolom_penggajian = ['ID','Nama','Posisi','Password','durasi_jam','Ongkos_Lembur','Potongan_Telat','Potongan_Absensi','Gaji_Pokok','Gaji_Bersih']
            # Membuat DataFrame Pandas dari data penggajian
            df = pd.DataFrame([entry.strip().split(',') for entry in data_penggajian[1:]], columns=kolom_penggajian)
            # Filter DataFrame berdasarkan ID yang sudah login
            filtered_df = df.loc[df['ID'] == str(launch_ID)]


            # Menampilkan data pada slip gaji
            if not filtered_df.empty:
                data = filtered_df.iloc[0]
                print(f"ID Karyawan    : {data['ID']}")
                print(f"Nama           : {data['Nama']}")
                print(f"Posisi         : {data['Posisi']}")
                print("-"*86)
                print(f"Gaji Pokok     : Rp {float(data['Gaji_Pokok']):,.2f}")
                print(f"Ongkos Lembur  : Rp {float(data['Ongkos_Lembur']):,.2f}")
                print(f"Potongan Telat : Rp {float(data['Potongan_Telat']):,.2f}")
                print(f"Potongan Absen : Rp {float(data['Potongan_Absensi']):,.2f}")
                print("-"*86)
                print(f"Gaji Bersih    : Rp {float(data['Gaji_Bersih']):,.2f}")
                input("="*86 + "\n")
            else:
                input("Data penggajian tidak ditemukan untuk ID ini.")
            main_page_employee()


        cetak_slip(launch_ID)
    
    # FITUR 6

    elif menu_choice == '7':  # FITUR 7 EULA
        os.system('cls')
        print(eula_text)
        input("\nTekan [enter] untuk kembali ke menu utama")
        main_page_employee()    # MENGEMBALIKAN KE MENU UTAMA

    # FITUR 6 SELESAI - UI : COMMENT : DESAIN

    elif menu_choice == '8':  # FITUR 8 KELUAR
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

    # apabila database presensi admin belum ada
    if not(Path('presensi_database_admin.csv').is_file()):
        #buat file dahulu sebelum mengakses fungsi tambah supaya bisa menambahkan header dulu
        presensi = open('presensi_database_admin.csv', 'w')
        presensi.close()

    # apabila database presensi employee belum ada
    if not(Path('presensi_database.csv').is_file()):
        #buat file dahulu sebelum mengakses fungsi tambah supaya bisa menambahkan header dulu
        presensi = open('presensi_database.csv', 'w')
        presensi.close()

    # apabila database histori belum ada
    if not(Path('histori_database.csv').is_file()):
        #buat file dahulu sebelum mengakses fungsi tambah supaya bisa menambahkan header dulu
        presensi = open('histori_database.csv', 'w')
        presensi.close()


    # apabila database perintah lembur belum ada
    if not(Path('perintah_lembur.csv').is_file()):
        #buat file dahulu sebelum mengakses fungsi tambah supaya bisa menambahkan header dulu
        employee = open('perintah_lembur.csv', 'w')
        employee.close()

    # apabila database presensi lembur belum ada
    if not(Path('employee_presensi_lembur.csv').is_file()):
        #buat file dahulu sebelum mengakses fungsi tambah supaya bisa menambahkan header dulu
        employee = open('employee_presensi_lembur.csv', 'w')
        employee.close()


    # apabila database gaji belum ada
    if not(Path('employee_penggajian.csv').is_file()):
        #buat file dahulu sebelum mengakses fungsi tambah supaya bisa menambahkan header dulu
        employee = open('penggajian_database.csv', 'w')
        employee.close()
    

    # apabila database akun karyawan belum ada
    if not(Path('employee_account_database.csv').is_file()):
        #buat file dahulu sebelum mengakses fungsi tambah supaya bisa menambahkan header dulu
        employee = open('employee_account_database.csv', 'w')
        employee.close()

    # apabila database admin belum ada
    if not(Path('admin_account_database.csv').is_file()):
        #buat file dahulu sebelum mengakses fungsi tambah supaya bisa menambahkan header dulu

        # data admin pertama
        first_account_ID     = str(input("Anda adalah admin pertama! \nMasukkan ID anda           : "))
        first_account_nama   = str(input("Masukkan Nama Lengkap anda : "))
        first_account_posisi = str(input("Masukkan Jabatan anda      : "))
        first_Account_pass   = str(input("Masukkan passkey anda      : "))

        # memasukkan admin pertama 
        first_input = f"{first_account_ID.upper()},{first_account_nama.upper()},{first_account_posisi.upper()},{first_Account_pass}"

        with open('admin_account_database.csv', 'w', newline='') as fileAdmincsv:
            admin_list = csv.DictWriter(fileAdmincsv, fieldnames=[first_input],  delimiter='/') 
            admin_list.writeheader()

# FITUR AKUN PERTAMA SELESAI

# ------------------------------------------------------------------------------------------------------------------------------------------------------------



# BACKEND : OTOMATIS PRESENSI BILA TIDAK HADIR------------------------------------------------------------------------------------------------------------------

def backendAutoPresensi():
    # MEMBUAT PENGECEK DATA PRESENSI SUDAH ADA ATAU BELUM

    # MENGIMPOR DATA ADMIN
    data_admin = []     # VARIABEL KOSONG UNTUK MENYIMPAN DATA ADMIN
    with open('admin_account_database.csv') as csvfile_admin:       # MEMBUKA .CSV ADMIN
        reader_Admin = csv.reader(csvfile_admin)
        for row in reader_Admin:        # menjadikan file .csv menjadi list admin (menambahkan tiap baris pada .csv kedalam variabel data admin)
            data_admin.append(row)
    
    # DATABASE PRESENSI ADMIN
    data_presensi_admin = []
    with open('presensi_database_admin.csv') as csvfile_presensi:
        reader_presensi = csv.reader(csvfile_presensi)
        for row in reader_presensi:
            data_presensi_admin.append(row)

    # INDIKATOR DATABASE PRESENSI ADMIN
    data_presensi_admin_cond = []
    g=0
    with open('presensi_database_admin.csv') as csvfile_presensi:
        reader_presensi = csv.reader(csvfile_presensi)
        for row in reader_presensi:
            data_presensi_admin_cond.append(row)
            data_presensi_admin_cond[g][-1] = ""
            data_presensi_admin_cond[g][-2] = ""
            g+=1

    # INDIKATOR DATABASE KARYAWAN
    data_employee = []
    with open('employee_account_database.csv') as csvfile_employee:
        reader_employee = csv.reader(csvfile_employee)
        for row in reader_employee:
            data_employee.append(row)

    # DATABASE PRESENSI EMPLOYEE
    data_presensi = []
    with open('presensi_database.csv') as csvfile_presensi:
        reader_presensi = csv.reader(csvfile_presensi)
        for row in reader_presensi:
            data_presensi.append(row)

    # INDIKATOR DATABASE PRESENSI EMPLOYEE
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

    # MENGIMPOR DATA PERINTAH LEMBUR
    data_perintah_lembur = [] 
    with open('perintah_lembur.csv') as csvfile_perintah_lembur:    
        reader_perintah_lembur = csv.reader(csvfile_perintah_lembur)
        for row in reader_perintah_lembur:
            data_perintah_lembur.append(row)

    # MENGIMPOR DATA PRESENSI LEMBUR
    data_presensi_lembur = []
    with open('employee_presensi_lembur.csv') as csvfile_presensi_lembur: 
        reader_presensi_lembur = csv.reader(csvfile_presensi_lembur)      
        for row in reader_presensi_lembur:
            data_presensi_lembur.append(row)

    # INDIKATOR DATABASE PRESENSI LEMBUR
    data_presensilembur_cond = []
    g=0
    with open('presensi_database.csv') as csvfile_presensilembur:
        reader_presensilembur = csv.reader(csvfile_presensilembur)
        for row in reader_presensilembur:
            data_presensilembur_cond.append(row)
            data_presensilembur_cond[g][-1] = ""
            data_presensilembur_cond[g][-2] = ""
            g+=1

    # MULAI EKSEKUSI BACKEND

    if datetime.datetime.now().strftime("%HH:%MM:%SS") > close_kerja:

        # AUTOABSEN PRESENSI ADMIN
        for tujuan in range (0, len(data_admin)):

            hari_seminggu = ["SENIN", "SELASA", "RABU", "KAMIS", "JUMAT", "SABTU", "MINGGU"]
            hari_seminggu_inggris = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
            for nomor_hari in range(0,7):
                if (datetime.datetime.now().strftime("%A").upper() == hari_seminggu_inggris[nomor_hari]):   

                    data_baru = [tanggal_presensi, data_admin[tujuan][0], data_admin[tujuan][1], hari_seminggu[nomor_hari],'TIDAK HADIR',datetime.datetime.now().strftime("%H:%M:%S")]
                    data_baru_cond = [f'{tanggal_presensi}', f'{data_admin[tujuan][0]}', f'{data_admin[tujuan][1]}', hari_seminggu[nomor_hari], '', '']
                    dataUpdateHistori = [f'{backend_tanggal_presensi} Karyawan {data_admin[tujuan][0]} {data_admin[tujuan][1]} tidak presensi']

                    if (data_baru_cond not in data_presensi_admin_cond) and ((datetime.datetime.now().strftime("%H:%M:%S") ) not in (pre_presensi and time_range_kerja)) and (dataUpdateHistori not in dataHistory):
                        data_presensi_admin.append(data_baru)   # Menambahkan data baru ke dalam list data_presensi
                        with open('presensi_database_admin.csv', 'w', newline='') as csvfile_presensi:    # Membuka file CSV dalam mode penulisan dan menulis data baru ke dalamnya
                            writer_presensi = csv.writer(csvfile_presensi)
                            writer_presensi.writerows(data_presensi)
                        with open('histori_database.csv', 'a', newline='') as csvfile_histori:    # notifikasi ke admin
                            writer_histori = csv.writer(csvfile_histori,quoting=csv.QUOTE_NONE, escapechar='_')
                            writer_histori.writerows([dataUpdateHistori])
                    else:
                        pass

        # AUTOABSEN PRESENSI EMPLOYEE
        for tujuan in range (0, len(data_employee)):

            hari_seminggu = ["SENIN", "SELASA", "RABU", "KAMIS", "JUMAT", "SABTU", "MINGGU"]
            hari_seminggu_inggris = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
            for nomor_hari in range(0,7):
                if (datetime.datetime.now().strftime("%A").upper() == hari_seminggu_inggris[nomor_hari]):   

                    data_baru = [tanggal_presensi, data_employee[tujuan][0], data_employee[tujuan][1], hari_seminggu[nomor_hari],'TIDAK HADIR',datetime.datetime.now().strftime("%H:%M:%S")]

                    data_baru_cond = [f'{tanggal_presensi}', f'{data_employee[tujuan][0]}', f'{data_employee[tujuan][1]}', hari_seminggu[nomor_hari], '', '']

                    dataUpdateHistori = [f'{backend_tanggal_presensi} Karyawan {data_employee[tujuan][0]} {data_employee[tujuan][1]} tidak presensi']

                    if (data_baru_cond not in data_presensi_cond) and ((datetime.datetime.now().strftime("%H:%M:%S") ) not in (pre_presensi and time_range_kerja)) and (dataUpdateHistori not in dataHistory):
                        data_presensi.append(data_baru)   # Menambahkan data baru ke dalam list data_presensi
                        with open('presensi_database.csv', 'w', newline='') as csvfile_presensi:    # Membuka file CSV dalam mode penulisan dan menulis data baru ke dalamnya
                            writer_presensi = csv.writer(csvfile_presensi)
                            writer_presensi.writerows(data_presensi)
                        with open('histori_database.csv', 'a', newline='') as csvfile_histori:    # notifikasi ke admin
                            writer_histori = csv.writer(csvfile_histori,quoting=csv.QUOTE_NONE, escapechar='_')
                            writer_histori.writerows([dataUpdateHistori])
                    else:
                        pass
        
        # AUTOABSENSI PRESENSI LEMBUR
        if datetime.datetime.now().strftime("%HH:%MM:%SS") > close_lembur:
            hari_seminggu = ["SENIN", "SELASA", "RABU", "KAMIS", "JUMAT", "SABTU", "MINGGU"]
            hari_seminggu_inggris = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
            
            data_baru_lembur = []

            for nomor_hari in range(0,7):
                if (datetime.datetime.now().strftime("%A").upper() == hari_seminggu_inggris[nomor_hari]):  
                    for tujuan_lembur in range (0, len(data_perintah_lembur)):
                        data_baru_lembur_kotak = []
                        data_baru_lembur_kotak = ([f'{tanggal_presensi}', f'{data_perintah_lembur[tujuan_lembur][2]}', f'{data_perintah_lembur[tujuan_lembur][3]}', f'{hari_seminggu[nomor_hari]}', "TIDAK HADIR", f'{datetime.datetime.now().strftime("%H:%M:%S")}'])
                        data_baru_cond = [f'{tanggal_presensi}',f'{hari_seminggu[nomor_hari]}', f'{data_perintah_lembur[tujuan_lembur][2]}', f'{data_perintah_lembur[tujuan_lembur][3]}', '', '', '']
                        dataUpdateHistori = [f'{backend_tanggal_presensi} Karyawan {data_perintah_lembur[tujuan_lembur][2]} {data_perintah_lembur[tujuan_lembur][3]} tidak lembur']

                        if (data_baru_cond not in data_presensilembur_cond) and ((datetime.datetime.now().strftime("%H:%M:%S") ) not in (pre_presensi and time_range_kerja and DateTimeRange(data_perintah_lembur[tujuan_lembur][-3], data_perintah_lembur[tujuan_lembur][-2]))) and (dataUpdateHistori not in dataHistory):
                            data_baru_lembur.append(data_baru_lembur_kotak)   # Menambahkan data baru ke dalam list data_presensi
                            with open('employee_presensi_lembur.csv', 'w', newline='') as csvfile_presensi_lembur:    # Membuka file CSV dalam mode penulisan dan menulis data baru ke dalamnya
                                writer_presensi_lembur = csv.writer(csvfile_presensi_lembur)
                                writer_presensi_lembur.writerow(data_baru_lembur_kotak)
                            with open('histori_database.csv', 'a', newline='') as csvfile_histori:    # notifikasi ke admin
                                writer_histori = csv.writer(csvfile_histori,quoting=csv.QUOTE_NONE, escapechar='_')
                                writer_histori.writerows([dataUpdateHistori])
                        else:
                            pass
       


# BACKEND : OTOMATIS PRESENSI BILA TIDAK HADIR SELESAI

# ------------------------------------------------------------------------------------------------------------------------------------------------------------


# PERKOLOMAN DAN DESAIN---------------------------------------------------------------------------------------------------------------------------------------

# kolom esensial
kolom_admin    = ['ID','Nama','Posisi','Password']
kolom_employee = ['ID','Nama','Posisi','Password']
kolom_presensi = ["Tanggal", "ID", "Nama", "Hari Kerja", "Kehadiran", "Waktu"]
kolom_penggajian = ["ID", "Nama", "Posisi", "Gaji Pokok", "Ongkos Lembur", "Potongan Absensi", "Gaji Bersih" ]
kolom_lembur   = ["Tanggal","Hari","ID","Nama","Jam Mulai","Jam Selesai","durasi_jam"]

kolom_fmt = "grid"

# lama freeze welcome page
delayWelcome = 0

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

# range jam kerja
time_range_kerja = DateTimeRange("08:00:00", "16:59:59")
pre_presensi = DateTimeRange("00:00:00", "07:59:59")
open_presensi = "08:00:00"
close_presensi = "08:59:59"
close_kerja = "17:00:00"
close_lembur = "23:59:59"
global_close_presensi = "23:59:59"

# untuk absensi otomatis
waktuRealBackend = now_time.strftime("%A %d %B %Y")
backend_tanggal_presensi = datetime.datetime.now().strftime("%Y-%m-%d %A")

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
