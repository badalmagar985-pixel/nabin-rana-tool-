import os
import time

def banner():
    os.system('clear')
    print("\033[1;31m  _   _          _     _              ")
    print(" | \ | |   __ _ | |__ (_) _ __        ")
    print(" |  \| |  / _` || '_ \| || '_ \       ")
    print(" | |\  | | (_| || |_) || || | | |      ")
    print(" |_| \_|  \__,_||_.__/ |_||_| |_|      ")
    print("      R  A  N  A    T  O  O  L  S     \033[0m")
    print("=======================================")
    print("  Author  : NABIN RANA                 ")
    print("  Github  : github.com/nabin-rana      ")
    print("  Version : 1.0 (World Best Edition)   ")
    print("=======================================")

def menu():
    banner()
    print("\033[1;32m [01] Free Fire ID Cloning (FB/VK)")
    print(" [02] CCTV Password Cracker (RTSP)")
    print(" [03] Update Tool")
    print(" [00] Exit\033[0m")
    
    choice = input("\n[+] Select Option: ")
    if choice == '01':
        print("\n[!] Cloning Start bhayo... Please Wait...")
        # Yaha tapai ko cloning logic (brute force) huncha
    elif choice == '02':
        print("\n[!] Scanning CCTV Passwords...")
        # Yaha CCTV crack garne logic huncha
    else:
        print("\nBye Bye!")

if __name__ == "__main__":
    menu()

