from pyfiglet import Figlet
from colorama import init, Fore, Style
import random

#Initialize colorama
init(autoreset=True)

colors = [
    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.CYAN
]

def main():
    print(Fore.CYAN + "===Colorful ASCII Generator ===")

    text = input("Enter text: ")

    f = Figlet()

    print("\nSample fonts: slant, block, banner, standard, big")
    font_choice = input("Choose font: ")

    try:
        f.setFont(font=font_choice)
    except:
        print(Fore.RED + "Invalid font! Using default.")

    ascii_art = f.renderText(text)

    print("\nGenerator ASCII Art:\n")

    for line in ascii_art.split("\n"):
        print(random.choice(colors) + line)

        main()
