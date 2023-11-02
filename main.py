import os

from stock_pupuk import pupuk
from penjadwalan_pupuk import p
from perhitungan_pupuk import homepage

def awal():
    print("-"*35)
    print("|", "Alikasi Manajemen Pupuk".center(31).upper(), "|" )
    print("|", "By Kelompok 1".center(31).upper(), "|")
    print("-"*35)
    print("1. STOCK PUPUK \n2. PENJADWALAN KEGIATAN \n3. PERHITUNGAN PUPUK")

    tanya = int(input("Pilih Fitur Yang Ingin Anda Gunakan : "))

    if tanya == 1:
        os.system('cls')
        while True:
            pupuk()
            x = input("Apakah anda ingin mengulang program (y/t) : ").lower()
            if x == "y":
                os.system('cls')
                continue
            else:
                break
    elif tanya == 2 :
        os.system('cls')
        while True:
            p()
            x = input("Apakah anda ingin mengulang program (y/t) : ").lower()
            if x == "y":
                os.system('cls')
                continue
            else:
                break
    elif tanya == 3 :
        os.system('cls')
        while True:
            homepage()
            x = input("Apakah anda ingin mengulang program (y/t) : ").lower()
            if x == "y":
                os.system('cls')
                continue
            else:
                break

while True:
    awal()
    back_to_home = input("Apakah anda ingin Kembali Ke Beranda (y/t) : ").lower()
    if back_to_home == "y":
        os.system('cls')
        continue
    else:
        break