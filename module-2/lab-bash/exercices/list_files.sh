#!/bin/bash

# Ejericio número uno

ls
mkdir new_dir
rm new_dir -r
cp ../lorem/sed.txt ../lorem-copy
cp ../lorem/at.txt ../lorem-copy; cp ../lorem/sed.txt ../lorem-copy
cat ../lorem/sed.txt
cat ../lorem/at.txt ../lorem/lorem.txt
head ../lorem-copy/sed.txt -n 3
tail ../lorem-copy/sed.txt -n 3
echo "Homo homini lupus." >> ../lorem-copy/sed.txt
sed 's/et/ET/g' ../lorem-copy/at.txt
whoami
pwd
ls ../lorem/*.txt
wc -l ../lorem/sed.txt 
# encuentra el número de archivos que comienzan por lorem en este directorio incluidas subcarpetas
find ../. -type f -name "lorem*" | wc -l
# cuenta las veces que aparece 'et' en at.txt
grep -ow 'et' ../lorem/at.txt | wc -l
# cuenta las veces que aparece 'et' en todos lo archivos del directorio lorem-copy
find ../lorem-copy -type f | xargs grep -ow "et" | wc -l

# Ficheros BASH
# ya esta

# Bonus

name='Yuver'
echo $name
mkdir $name
rm -r $name

for i in $( ls ../lorem ); do
	k=${i%.txt}
	echo $k has ${#k}  characters lenght
done

# Mostrar procesos
# top
# htop
# ps -e
# ps -ef
# ps -elij

# Mostar info de procesador
# less  /proc/cpuinfo
# lscpu
# lshw -class processor

# Los alias:
# alias gpom="git push origin master"
# alias html="cd /var/www/html"
# alias logs="cd /var/logs/apache2"

# Comprime carpetas
# tar -zcvf lorem-compressed.tar.gz ../lorem ../lorem-copy
# Descomprime carpetas
# mkdir ../lorem-uncompressed
# tar -xvf lorem-compressed.tar.gz -C ../lorem-uncompressed\n

