import sys
from PIL import Image, ImageOps
import os


def main():
    check(sys.argv)

    shirt = Image.open("shirt.png")
    input_image = ImageOps.fit(Image.open(sys.argv[1]), shirt.size)
    input_image.paste(shirt, shirt)
    input_image.save(sys.argv[2])


def check(argv):
    if len(argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 3:
        sys.exit("Too few command-line arguments")
    else:
        pass

    input_format = os.path.splitext(argv[1])[1]
    output_format = os.path.splitext(argv[2])[1]

    if input_format != ".jpg" and input_format != ".jpeg" and input_format != ".png":
        sys.exit("Invalid input")
    if output_format != ".jpg" and output_format != ".jpeg" and output_format != ".png":
        sys.exit("Invalid output")

    if input_format != output_format:
        sys.exit("Input and output have different extensions")

    try:
        f = open(argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
