
print("Tugas Projek SISOP Kelas A")
print("------------------------------------------------")

print("-----MENU-----")
print("1, penjumlahan")
print("2. pengurangan")
print("3. perkalian")
print("4. pemangkatan")
print("----------------")
pilih = int(input("pilih: "))

a = int(input("masukkan nilai a: "))
b = int(input("masukkan nilai b: "))
if pilih == 1:
   hasil_1 = a + b
   print("hasil = ",hasil_1)
elif pilih == 2:
   hasil_2 = a - b
   print("hasil = ",hasil_2)
elif pilih == 3:
   hasil_3 = a * b
   print("hasil = ",hasil_3)
elif pilih == 4:
   hasil_4 = a ** b
   print("hasil = ",hasil_4)
