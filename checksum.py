import sys
import os
import hashlib

file_to_check = input("Enter the path of the file to check:") 

hash_alg = input("Which hash algorithm would you like to use? Options are: MD5, SHA1, SHA256, SHA512")

if (hash_alg == "MD5" or hash_alg == "md5"):
    checksum = hashlib.md5(open('{0}'.format(file_to_check),'rb').read()).hexdigest() #opens the file as a hexdigest so the checksum will be of the file CONTENTS not filename
    print(checksum)

elif (hash_alg == "SHA1" or hash_alg == "sha1"):
    checksum = hashlib.sha1(open('{0}'.format(file_to_check),'rb').read()).hexdigest() 
    print(checksum)  

elif (hash_alg == "SHA256" or hash_alg == "sha256"):
    checksum = hashlib.sha256(open('{0}'.format(file_to_check),'rb').read()).hexdigest() 
    print(checksum)  

elif (hash_alg == "SHA512" or hash_alg == "sha512"):
    checksum = hashlib.sha512(open('{0}'.format(file_to_check),'rb').read()).hexdigest() 
    print(checksum)        


################################# Compare checksum code ###################################

compare = input("Do you want to compare this checksum? y or n ")

if (compare == 'y'):
    checksum_to_compare = input("Please enter the checksum to compare against: ")   
    
    if (checksum_to_compare == checksum):
        print("Congrats! They match!")
    else:
        print("Uh Oh, they don't match")

else:
    print("Have a nice day")


# Hotanya Ragtah - 2018
