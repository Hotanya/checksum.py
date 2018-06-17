# checksum.py
checksum.py is a simple script which I had the idea to write when I wanted to verify a downloaded file. Initially the script made use of os.system to run certutil, however it was very difficult to compare against a user provided checksum. The latest version makes use of hashlib (much SIMPLER and POWERFUL) and allows the user to verify and compare MD5, SHA1, SHA256, SHA512 checksums 
