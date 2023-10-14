def main():
    g = input("Greeting: ")
    print(f"${value(g)}")


def value(greeting):
    greeting = greeting.lower().split()
    if "hello" in greeting[0]:
        return 0
    elif greeting[0][0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
