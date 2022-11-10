from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

batas = int(input("masukkan batas perulangan : "))

def cetak(i):
    for i in range(1, batas+1):
        if i % 2 == 1:
           print(i, "ganjil", "- ID proses", getpid())
           continue
        print(i, "genap", "- ID proses", getpid())
    sleep(1)

print("sekuensial")

sekuensial_awal = time()

for i in range(1):
    cetak(i)

sekuensial_akhir = time()
print()

print("multiprocessing.Process")

kumpulan_proses = []

process_awal = time()

for i in range(1):
    p = Process(target=cetak, args=(i,))
    kumpulan_proses.append(p)
    p.start()

for i in kumpulan_proses:
    p.join()

process_akhir = time()
print()

print("multiprocessing.Pool")

pool_awal = time()

pool = Pool()
pool.map(cetak, range(0,1))
pool.close()

pool_akhir = time()
print()

print("Waktu eksekusi sekuensial :", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu multiprocessing.Process :", process_akhir - process_awal, "detik")
print("Waktu multiprocessing.Pool :", pool_akhir - pool_awal, "detik")
