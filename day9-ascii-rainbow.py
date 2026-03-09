import time
import random
from pyfiglet import Figlet
from colorama import init, Fore, Style

#initialize colorama
init(autoreset=True)
colors = [
    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.CYAN
]

#FONTS YOU CAN CHOOSE
fonts = ["slant", "block", "banner", "standard", "big"]

def rainbow_ascii(text, font="slant",speed=0.05):
    f = Figlet(font=font)
    ascii_art = f.renderText(text)

    #Loop through each line
    for line in ascii_art.split("\n"):
        #Random color per line
        print(random.choice(colors) + line)

        time.sleep(speed)

def main():
    print(Fore.CYAN + "=== Animated Rainbow ASCII Generator ===\n")
    text = input("Enter text to generate:")

    print("\nAvailable fonts: slant, block, banner, standard, big")
    font_choice = input("Choose font (or leave empty for default): ")

    if font_choice not in fonts:
        font_choice = "slant"

    print("\nGenerating....\n")
    rainbow_ascii(text, font=font_choice, speed=0.03)

if __name__ == "__main__":
     main()

