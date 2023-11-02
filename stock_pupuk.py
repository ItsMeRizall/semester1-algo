import pandas as pd
import os
import datetime
import prettytable
from penjadwalan_pupuk import hiasan

head_data = ["tanggal","pupuk","pemasukan","pengeluaran","Stock Awal","Stock Akhir", "ket"]

def pupuk():
    source = os.path.join(os.getcwd(), "pupuk.csv")
    df = pd.read_csv(source)

    hiasan('PENCATATAN STOCK PUPUK', 40, "=", 40)
    print("1. Stock Pupuk\n2. Masukkan Jumlah Pupuk Baru\n3. Mengambil Data" )
    x = int(input("Masukkan Pilihan anda >>  "))

    if x == 1:
        with open(source) as fp:
            print(prettytable.from_csv(fp))
    elif x == 2:
        with open(source) as fp:
            print(prettytable.from_csv(fp))
        tampung = []
        nama_pupuk = input("Masukkan Nama Pupuk : ")
        berat = int(input("Masukkan Berat Pupuk : "))
        ket = input("Masukkan Keterangan : ")

        date = waktu.strftime("%x")
        list_pupuk = lambda dataframe, column : dataframe[column].tolist()      

        if nama_pupuk in list_pupuk(df,'pupuk'):
            replace_old_dataPemasukan(source, df, tampung, nama_pupuk, berat, ket, date, list_pupuk)

        else :
            add_new_data(source, tampung, nama_pupuk, berat, ket, date)
    
    elif x == 3:
        with open(source) as fp:
            print(prettytable.from_csv(fp))
        tampung = []
        nama_pupuk = input("Masukkan Nama Pupuk : ")
        berat = int(input("Masukkan Berat Pupuk : "))
        ket = input("Masukkan Keterangan : ")

        date = waktu.strftime("%x")
        list_pupuk = lambda dataframe, column : dataframe[column].tolist()

        replace_old_dataPengeluaran(source, df, tampung, nama_pupuk, berat, ket, date, list_pupuk)
    
    else:
        hiasan("MASUKKAN ANGKA 1, 2 , 3", 40, "=", 40)

def replace_old_dataPengeluaran(source, df, tampung, nama_pupuk, berat, ket, date, list_pupuk):
    j = df.loc[(df['pupuk'].isin([nama_pupuk]))]
    replace = df.drop(j.index)

    replace.to_csv(source, mode='w', header=head_data, index=False)

    ttl_pupuk = list_pupuk(j, 'Stock Akhir')

    k = 0
    for i in ttl_pupuk:
        k = i
    
    total_akhir = k - berat

    new_data = [str(date), nama_pupuk, "-", berat, k ,total_akhir, ket]
    tampung.append(new_data)
    after(source, tampung)

def replace_old_dataPemasukan(source, df, tampung, nama_pupuk, berat, ket, date, list_pupuk):
    j = df.loc[(df['pupuk'].isin([nama_pupuk]))]
    replace = df.drop(j.index)

    replace.to_csv(source, mode='w', header=head_data, index=False)

    ttl_pupuk = list_pupuk(j, 'Stock Akhir')

    k = 0
    for i in ttl_pupuk:
        k = i + berat
            
    new_data = [str(date), nama_pupuk, berat,"-", ttl_pupuk[0] ,k, ket]
    tampung.append(new_data)
    after(source, tampung)

def add_new_data(source, tampung, nama_pupuk, berat, ket, date):
    new_data1 = [str(date), nama_pupuk, berat, "-", berat, berat,  ket]
            
    tampung.append(new_data1)

    add(source, tampung)
    

def add(source, tampung):
    add = pd.DataFrame(tampung)
    add.to_csv(source, mode='a', index=False, header=False)

def after(source, tampung):
    add = pd.DataFrame(tampung)
    add.to_csv(source, mode='a', index=False, header=False)

# pupuk()

waktu = datetime.datetime.today()

