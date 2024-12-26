# #!/usr/bin/env python3
#----------------------------------------------------------------
#
# Program python sederhana untuk meng-crack file ZIP
#
# Program ini menggunakan teknik Dictionary Attack
# dimana jika tidak ada kata sandi didalam file Wordlist
# Maka tidak bisa untuk meng-crack file ZIP
#
# Disclaimer
#
# Program ini dibuat hanya untuk tujuan edukasi dan pembelajaran
#
#----------------------------------------------------------------

# Import modul
import os
import sys
import pyzipper
import platform
from datetime import datetime

def cek_sistem_operasi():
        cek_os = platform.system()
        if cek_os == "Windows":
                os.system("cls")
        else:
                os.system("clear")

def banner():
        print("""
===============================================
       PROGRAM UNTUK MENG-CRACK FILE ZIP

  HANYA UNTUK TUJUAN EDUKASI DAN PEMBELAJARAN

       JANGAN DISALAHGUNAKAN YA BROO :)
===============================================
""")

def crack_dong_zip_nya(file_zip, file_wordlist, dir_hasil_crack):
        kata_sandi_ditemukan = False
        try:
                with pyzipper.AESZipFile(file_zip) as fz:
                        # File Wordlist
                        try:
                                with open(file_wordlist, "r") as fw:
                                        # Iterasi Kata sandi
                                        for kata_sandi in fw:
                                                kata_sandi = kata_sandi.strip()
                                                # Mencoba crack file ZIP
                                                try:
                                                        fz.extractall(pwd=kata_sandi.encode("utf-8"), path=dir_hasil_crack)
                                                        print(f"[+] Kata sandi ditemukan: {kata_sandi}")
                                                        print(f"[+] File ZIP berhasil di-crack dan disimpan di direktori: {dir_hasil_crack}")
                                                        kata_sandi_ditemukan = True
                                                        break
                                                except Exception:
                                                        print(f"[-] Kata sandi salah: {kata_sandi}")
                                                        continue
                        # File Wordlist tidak ditemukan
                        except FileNotFoundError:
                                print("[-] File Wordlist tidak ditemukan.")
                                sys.exit(1)
                        except Exception as error:
                                print(f"[-] Terjadi kesalahan yang tidak terduga: {error}")
                                sys.exit(1)
                if not kata_sandi_ditemukan:
                        print("[-] File ZIP gagal di-crack.")
                        sys.exit(1)
        # File ZIP tidak ditemukan
        except FileNotFoundError:
                print("[-] File ZIP tidak ditemukan.")
                sys.exit(1)
        except Exception as error:
                print(f"[-] Terjadi kesalahan yang tidak terduga: {error}")
                sys.exit(1)

if __name__ == "__main__":
        cek_sistem_operasi()
        banner()
        # Input file ZIP
        try:
                masukkan_file_zip = input("[#] Masukkan nama file ZIP: ")
                if not os.path.isfile(masukkan_file_zip):
                        print("[-] File ZIP tidak ditemukan.")
                        sys.exit(1)
        except KeyboardInterrupt:
                print("[-] Keluar program.")
                sys.exit(1)
        # Input file Wordlist
        try:
                masukkan_file_wordlist = input("[#] Masukkan nama file Wordlist: ")
                if not os.path.isfile(masukkan_file_wordlist):
                        print("[-] File Wordlist tidak ditemukan.")
                        sys.exit(1)
        except KeyboardInterrupt:
                print("[-] Keluar program.")
                sys.exit(1)
        # Input Dir hasil Cracking
        try:
                masukkan_dir = input("[#] Masukkan nama direktori untuk menyimpan hasil cracking: ")
                if not os.path.isdir(masukkan_dir):
                        # Membuat direktori untuk menyimpan hasil Cracking
                        os.makedirs(masukkan_dir)
        except KeyboardInterrupt:
                print("[-] Keluar program.")
                sys.exit(1)

        crack_dong_zip_nya(masukkan_file_zip, masukkan_file_wordlist, masukkan_dir)
