import random
import sys

from pyfiglet import Figlet


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    # Expect zero or exactly two command-line arguments
    if len(sys.argv) == 1:
        # No arguments: pick a random font
        font = random.choice(fonts)
    elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font"):
        font = sys.argv[2]
        if font not in fonts:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

    figlet.setFont(font=font)

    text = input("Input: ")
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()
