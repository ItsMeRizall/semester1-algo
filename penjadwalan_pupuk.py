import pandas as pd
import os
import time
import datetime
import csv
import prettytable

header = ["No","Tanggal","Kegiatan", "Nama kegiatan", "Tanggal Kegiatan", "Ket"]
# file = open(os.path.join(os.getcwd,"Jadwal Pupuk","Jadwal.csv"))

listFolder = os.listdir()
if "jadwal.csv" in listFolder:
    pass
else: 
    with open("jadwal.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(header)

def tanggal_kegiatan(year:int, month:int, day:int):
    hari_kegiatan = datetime.datetime(year, month, day)
    hari_kegiatan = hari_kegiatan.strftime("%x")
    return hari_kegiatan

def date_today():
    date = datetime.datetime.today()
    date = date.strftime("%x")
    return date

def add(source, new_data, df):
    no = getIndex(df, "No")
    add = pd.DataFrame(new_data, index=[no])
    add.to_csv(source, mode='a' ,header=False)

def show_dataframe(source):
    with open(source, "r") as file:
        print(prettytable.from_csv(file))

def getIndex(dataframe, column:str):
    data = dataframe[column].tolist()
    k = 1
    for i in range(len(data)):
        k += 1
    return k

def hiasan(text:str, centerText:int, accesories:str, centerAccesories:int):
    print(" ")
    print(accesories*centerAccesories)
    print(text.center(centerText))
    print(accesories*centerAccesories)
    print(" ")

def p():
    source = os.path.join(os.getcwd(),"jadwal.csv")
    df = pd.read_csv(source)

    date = datetime.datetime.today()

    today = date_today()

    hiasan("AGENDA KEGIATAN", 40, "=", 40)

    print("1. Masukkan Agenda Baru\t\t\t", end=" ")
    print("2. Menghapus Agenda Lama")
    print("3. Mengecek Agenda Kegiatan")


    print(" ")
    tanya_user = int(input("Masukkan Pilihan Anda : "))
    print(" ")

    if tanya_user == 1:
        new_data = []

        show_dataframe(source)

        kegiatan = input("Masukkan Kegiatan Yang akan Di Lakukan : ")
        hari = int(input("Masukkan Tanggal Kegiatan : "))
        bulan = int(input("Masukkan Bulan Kegiatan : "))
        tahun = int(input("Masukkan Tahun Kegiatan : "))
        nama_tanaman = input("Masukkan Nama Tanaman : ")
        keterangan = input("Masukkan Keterangan Kegiatan : ")

        day_agenda = tanggal_kegiatan(tahun,bulan,hari)

        date1 = datetime.date(tahun, bulan , hari)
        date2 = datetime.date.today()
        
        hasil = date2 - date1

        conlucsion = int(hasil.days)
        if conlucsion >=  0:
            print(" ")
            print("Tangal sudah Kadaluarsa")
            print("Masukkan Tanggal Hari Ini Atau Kedepannya")

        else : 
            tampung = [today, kegiatan, day_agenda, nama_tanaman, keterangan]
            new_data.append(tampung)

            add(source, new_data, df)

    elif tanya_user == 2:
        show_dataframe(source)
        print (" ")
        delete = int(input("Data No Berapa Yang Ingin anda Hapus : "))
        lister = lambda dataframe, column: dataframe[column].tolist()

        data = lister(df, "No")

        if delete in data:
            tampung = []
            batas = len(data)
            for i in range(1, batas):
                tampung.append(i)
            df_delete = df.drop(columns=["No"])
            replace = pd.DataFrame(df_delete, index=tampung)
            with open("jadwal.csv", "w") as file:
                writer = csv.writer(file)
                writer.writerow(header)
            replace.to_csv(source, mode="a" , header=False)
            hiasan("DATA BERHASIL DI HAPUS", 40,"=", 40)
        else:
            hiasan("DATA TIDAK ADA", 40,"=", 40)

    elif tanya_user == 3 :
        show_dataframe(source)
    else :
        hiasan("Mohon Masukkan 1, 2 ,3",40,"=",40)
    

