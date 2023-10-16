import sys


def main():
    # check all possibilities of argument being invalid
    check(sys.argv)
    # count lines
    with open(sys.argv[1], "r") as file:
        lines = 0
        for line in file:
            if line.strip().startswith("#"):
                pass
            elif line.strip() == "":
                pass
            else:
                lines += 1
    print(lines)


def check(args):
    if len(args) < 2:
        sys.exit("Too few command-line argumets")
    elif len(args) > 2:
        sys.exit("Too many command-line arguments")

    if not args[1].endswith(".py"):
        sys.exit("Not a Python file")

    try:
        f = open(args[1], "r")
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        f.close()


if __name__ == "__main__":
    main()
