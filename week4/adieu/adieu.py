import inflect

p = inflect.engine()


names = []


def main():
    while True:
        try:
            name = input("Name: ")
        except EOFError:
            break
        else:
            names.append(name)
    print(f"Adieu, adieu, to {p.join(names)}")


if __name__ == "__main__":
    main()
