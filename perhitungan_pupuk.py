import pandas
import os
from penjadwalan_pupuk import hiasan

def homepage():
    hiasan("PERHITUNGAN PUPUK", 40, "-", 40)
    print(" ")
    print("Pilih Jenis Tanaman Yang Ingin Di Ketahui Dosis Pupuknya")
    print(" ")
    print("1. Jagung\t\t", end='')
    print("2. Padi")
    print("3. Cabe\t\t\t", end='')
    print("4. Terong")
    print(" ")

    choose()

def choose():
    pilih = int(input("Silahkan Pilih salah Satu : "))
    if pilih == 1:
        hitung_pupuk(350, 50, 400, 150, 200)
    elif pilih == 2:
        pupuk_padi(300, 100, 100)
    elif pilih == 3:
        pupuk_cabe()
    elif pilih == 4:
        pupuk_terong(80, 45)
    else :
        hiasan("ANGKA YANG ANDA MASUKKAN SALAH", 40, "-", 40)

def pupuk_terong(dosis_urea, dosis_kci):
    luas = int(input("Silahkan Masukkan luas Lahan Anda (m2 ): "))
    urea = dosis_pupuk(dosis_urea, luas)
    kci = dosis_pupuk(dosis_kci,luas)

    hiasan("TAKARAN TERONG", 40 , "=", 40)
    print("Dengan takaran Pupuk UREA  yang di dapat yaitu \t: ", urea, "Kg")
    print("Dengan takaran Pupuk KCI yang di dapat yaitu \t: ", kci , "Kg")

def pupuk_cabe():
    luas = int(input("Silahkan Masukkan luas Lahan Anda (m2 ): "))
    pupuk = dosis_pupuk(450,luas)

    hiasan("PUPUK CABE", 40, "-",40)
    print("Pupuk Yang Di Butuhkan Untuk Cabe : ", pupuk, "Kg")

def hitung_pupuk(dosis_urea,dosis_za,dosis_phonska,dosis_kci4,dosis_sp_36):
    luas = int(input("Silahkan Masukkan luas Lahan Anda (m2 ): "))
    urea = dosis_pupuk(dosis_urea, luas)
    za = dosis_pupuk(dosis_za,luas)
    phonska = dosis_pupuk(dosis_phonska, luas)
    Kci45 = dosis_pupuk(dosis_kci4, luas)
    sp_36 = dosis_pupuk(dosis_sp_36, luas)

    hasil(urea,za,phonska,Kci45,sp_36)
    
def dosis_pupuk(dosis, luas):
    hasil = (dosis/10000) * luas
    hasil = round(hasil, 2)
    return hasil

def pupuk_padi(dosis_urea,dosis_sp36,dosis_kci):
    luas = int(input("Silahkan Masukkan luas Lahan Anda (m2 ): "))

    hiasan("Untuk Padi Sendiri Menggunakan 3 Pupuk Kombinasi", 50 , "=", 50)
    urea = dosis_pupuk(dosis_urea, luas)
    sp36 = dosis_pupuk(dosis_sp36, luas)
    kci = dosis_pupuk(dosis_kci, luas)

    print("Dengan takaran pupuk Urea yang di dapat yaitu \t\t: ", urea, "Kg")
    print("Dengan takaran pupuk SP_36 yang di dapat yaitu \t\t: ", sp36, "Kg")
    print("Dengan takaran pupuk KCI yang di dapat yaitu \t\t: ", kci, "Kg")

    print("")

    pemakaian_pupuk_padi1(urea, sp36, kci)
    pemakaian_pupuk_padi2(urea)
    pemakaian_pupuk_padi3(urea, kci)

def pemakaian_pupuk_padi1(urea, sp36, kci):
    hiasan("Dengan Pupuk Pertama (7 - 10 HST) di perlukan :", 0 , "=", 50)
    print("Pupuk Urea Sebanyak \t: ",  (urea/4))
    print("Pupuk sp36 Sebanyak \t: ",  sp36)
    print("Pupuk KCI Sebanyak \t: ", kci/2)

def pemakaian_pupuk_padi2(urea):
    hiasan("Dengan Pupuk Kedua (21 HST) di perlukan :", 0 , "=", 50)
    print("Pupuk Urea Sebanyak \t: ",  (urea/2))

def pemakaian_pupuk_padi3(urea,kci):
    hiasan("Dengan Pupuk Ketiga (42 HST) di perlukan :", 0 , "=", 50)
    print("Pupuk Urea Sebanyak \t: ",  (urea/4))
    print("Pupuk KCI Sebanyak \t: ", kci/2)

def hasil(urea, za, phonska, kci45, sp_36):

    hiasan(">>> PUPUK JAGUNG <<<", 40 , "=", 40)
    print("Dengan Mennggunakan Pupuk Urea Maka Di Butuhkan \t\t : ", urea, " Kg")
    print("Dengan Mennggunakan Pupuk za Maka Di Butuhkan \t\t\t : ", za, " Kg")
    print("Dengan Mennggunakan Pupuk phonska Maka Di Butuhkan \t\t : ", phonska, " Kg")
    print("Dengan Mennggunakan Pupuk kci45 Maka Di Butuhkan \t\t : ", kci45, " Kg")
    print("Dengan Mennggunakan Pupuk sp_36 Maka Di Butuhkan \t\t : ", sp_36, " Kg")

