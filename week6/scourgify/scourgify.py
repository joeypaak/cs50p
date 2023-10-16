import sys
import csv

students = []


def main():
    check(sys.argv)

    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for student in reader:
            students.append(student)

    with open(sys.argv[2], "w") as file:
        dw = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        dw.writeheader()

        for student in students:
            last, first = map(str.strip, student["name"].split(","))
            house = student["house"]
            dw.writerow({"first": first, "last": last, "house": house})


def check(argv):
    if len(argv) < 3:
        sys.exit("Too few command-line argument")
    elif len(argv) > 3:
        sys.exit("Too many command-line argument")

    try:
        f1 = open(argv[1])
    except FileNotFoundError:
        sys.exit(f"Could not read {argv[1]}")
    else:
        f1.close()


if __name__ == "__main__":
    main()
