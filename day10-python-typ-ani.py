import time
import sys
from pyfiglet import figlet_format
from colorama import init, Fore

init()

def typing(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
typing(Fore.GREEN + "Booting System...")
time.sleep(1)

name = input("Enter your name: ")

ascii_text = figlet_format(name)

typing(Fore.CYAN + ascii_text, 0.002)