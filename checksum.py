import sys
import os

file_to_check = raw_input("Enter the path of the file to check:")

command = 'certutil -hashfile ' + file_to_check

hash_type = raw_input("Which Hash Algorithm do you want to check: HashAlgorithm choices: MD2 MD4 MD5 SHA1 SHA256 SHA384 SHA512 ")
command = "certutil -hashfile " + file_to_check + " " + hash_type

os.system('{0}'.format(command))


# Hotanya Ragtah - 2018
