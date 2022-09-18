#!/bin/bash

a = 20

echo -n "Hallo, masukkan nama anda : "
read nama;
echo "Selamat datang $nama";

echo -n "masukkan umur anda : "
read umur;
if umur == a
then
  echo "kita seumuran";
elif umur <= a
then
  echo "hai adeek";
else
echo "kita beda generasi";
fi
