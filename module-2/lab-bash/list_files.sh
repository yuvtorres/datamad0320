#!/bin/bash

# Ejericio número uno

ls
mkdir new_dir
rm new_dir -r
cp lorem/sed.txt lorem-copy
cp lorem/at.txt lorem-copy; cp lorem/sed.txt lorem-copy
cat lorem/sed.txt
cat lorem/at.txt lorem/lorem.txt
head lorem-copy/sed.txt -n 3
tail lorem-copy/sed.txt -n 3
echo "Homo homini lupus." >> lorem-copy/sed.txt
sed 's/et/ET/g' lorem-copy/at.txt
whoami
pwd
ls lorem/*.txt
wc -l lorem/sed.txt 
# encuentra el número de archivos que comienzan por lorem en este directorio incluidas subcarpetas
find . -type f -name "lorem*" | wc -l
# cuenta las veces que aparece 'et' en at.txt
grep -ow 'et' lorem/at.txt | wc -l


