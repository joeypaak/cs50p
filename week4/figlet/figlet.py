# Need to pip install pyfiglet
import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

fonts = figlet.getFonts()  # available fonts
fonts_count = len(fonts)  # 549


def main():
    # set random font
    if len(sys.argv) == 1:
        random_font = fonts[random.randrange(0, fonts_count)]
        figlet.setFont(font=random_font)

    # Check arguments and then set to specific font
    elif len(sys.argv) == 3:
        checkArgs(sys.argv[1], sys.argv[2])
        figlet.setFont(font=sys.argv[2])

    # quit figlet.py
    else:
        sys.exit("Invalid usage")

    # get user input and print the figlet version
    string = input("Input: ")
    print(f"Output:\n{figlet.renderText(string)}")


def checkArgs(a1, a2):
    if (a1 == "-f" or a1 == "--font") and a2 in fonts:
        pass
    else:
        sys.exit("Invalid usage")


if __name__ == "__main__":
    main()
