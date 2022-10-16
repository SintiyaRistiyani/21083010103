#!bin/bash

declare -a nilai;

echo
echo -n "batas nilai yang dimasukkan :"; read ipk

total=0;
ipkMhs=0;

echo
echo "======================="

for ((i=1; i<=ipk; 1++))
do
     echo
     echo -n "masukkan nilai ips ke $i : " ; read nilai [$i];
     let total=$total+${nilai[i]};
     let ipkMhs=$total/$ipk;
done

echo 
echo "+++++==========++++++++++===========++++++"
echo 
echo "nilai ips mahasiswa selama 3 semester"
echo
echo " >> ${nilai[@]} <<";
echo
echo " nilai ips: $total/$ipk";
echo
echo "nilai ipk: $nilaiMhs";

