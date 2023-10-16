import sys
import csv
from tabulate import tabulate

table = []
headers = []


def main():
    check(sys.argv)

    with open(sys.argv[1]) as file:
        firstLine = True
        for line in file:
            one, two, three = line.strip().split(",")
            if firstLine:

                headers.extend([one, two, three])
                firstLine = False
            else:
                table.append([one, two, three])
    print(tabulate(table, headers, tablefmt="grid"))


def check(argv):
    if len(argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 2:
        sys.exit("Too many command-line arguments")

    try:
        f = open(argv[1], "r")
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        f.close()

    if not argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
