import json
import os

NAMA_FILE = "todolist.json"



tugas_selesai = []
tugas_belum = []

def simpan_data():
    with open(NAMA_FILE, "w") as file:
        json.dump({"belum": tugas_belum, "selesai": tugas_selesai}, file, indent=4)


def muat_data():
    global tugas_belum, tugas_selesai
    if os.path.exists(NAMA_FILE):
        with open(NAMA_FILE, "r") as file:
            data = json.load(file)
            tugas_belum = data.get("belum", [])
            tugas_selesai = data.get("selesai", [])

def printTugas(tugas_list):
    for i, tugas in enumerate(tugas_list, start=1):
        print(f"{i}. {tugas['Nama Tugas']} (Deadline: {tugas['Deadline Tugas']} - Prioritas: {tugas['Prioritas Tugas']})")
    print("")
  

def menuTDL():
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Hapus Tugas")
    print("4. Tandai Tugas Selesai")
    print("5. Keluar")
    print("")

muat_data()

while True:
    print("=== To Do List ===\t\n")
    menuTDL()
    try:
        userInput = int(input("Pilih Menu: "))
        if userInput < 1 or userInput > 5:
            print("Pilih Menu Yang Tersedia!\t\n")
            continue
    except ValueError:
        print("Masukkan Angka!\t\n")
        continue
    if userInput == 1:
        nama_tugas = input("Masukkan Tugas: ").capitalize()
        deadline_tugas = input("Masukkan Deadline Tugas: ").capitalize()
        prioritas_tugas = input("Masukkan Prioritas Tugas: ").capitalize()
        tambah_tugas = {"Nama Tugas": nama_tugas, "Deadline Tugas": deadline_tugas, "Prioritas Tugas": prioritas_tugas}
        tugas_belum.append(tambah_tugas)
        simpan_data()
        print("Tugas Berhasil Ditambahkan")
    elif userInput == 2:
        if tugas_belum:
            print("Daftar Tugas Belum Selesai:")
            printTugas(tugas_belum)
        else:
            print("Tugas Belum Selesai Kosong")

        if tugas_selesai:
            print("Daftar Tugas Selesai:")
            printTugas(tugas_selesai)
        else:
            print("Tugas Selesai Kosong")
  
    elif userInput == 3:
        if tugas_belum:
            printTugas(tugas_belum)
            try:
                hapus_tugas = int(input("Tugas Nomor Berapa Yang Ingin Anda Hapus: "))
            except ValueError:
                print("Masukkan Angka!\t\n")
                continue
            if 1 <=hapus_tugas <= len(tugas_belum):
                del tugas_belum[hapus_tugas - 1]
                simpan_data()
                print("Tugas Berhasil Dihapus")
            else:
                print("Tugas Tidak Ada")
        else:
            print("Tugas Kosong")
            
    elif userInput == 4:
        if tugas_belum:
            printTugas(tugas_belum)
            try:
                tandai_tugas = int(input("Tugas Nomor Berapa Yang Ingin Anda Tandai Selesai: "))
            except ValueError:
                print("Masukkan Angka!\t\n")
                continue
            if 1 <= tandai_tugas <= len(tugas_belum):
                tugas_selesai.append(tugas_belum[tandai_tugas - 1])
                del tugas_belum[tandai_tugas - 1]
                simpan_data()
                print("Tugas Berhasil Ditandai Selesai")
            else:
                print("Tugas Tidak Ada")
        else:
            print("Tugas Kosong")
    
    elif userInput == 5:
        break